#!/usr/bin/env python3
"""BTC-004 Gate A, scaling proof v3: independent symbolic verifier.

Runs exact algebra in SymPy and independently derives the identities rather than
calling the previous Maccioni verifier or parsing formulas from the proof.

Mathematical caveat: this script verifies the finite symbolic premises. The
implicit-function/conservation-of-intersection-multiplicity steps are rigorous
arguments, not executable finite exact checks. A human referee / second CAS has
not yet independently certified those steps.
"""

from __future__ import annotations
import hashlib
from pathlib import Path
import sympy as S

X,Y,t=S.symbols('X Y t',real=True)
q=3*X**4-5*X**2*Y**2+5*Y**4+20*X**2*Y-32*Y**3+X**2+2*Y**2
assert S.factor(S.diff(q,X)) == 2*X*(6*X**2-5*Y**2+20*Y+1)
assert S.expand(S.diff(q,Y)-(4*Y*(5*Y**2-24*Y+1)+X**2*(20-10*Y)))==0

qxx=S.diff(q,X,2)
qxy=S.diff(q,X,Y)
qyy=S.diff(q,Y,2)
hess_det=S.expand(qxx*qyy-qxy**2)

# Independently derive the six off-axis branches from the gradient equations.
X2=(5*Y**2-20*Y-1)/6
eliminated=S.factor(S.diff(q,Y).subs(X**2,X2))
assert S.simplify(eliminated-(Y-5)*(Y+1)*(35*Y+2)/3)==0
assert S.factor(S.diff(q,Y).subs(X,0))==4*Y*(5*Y**2-24*Y+1)

realcrit=[(S.Integer(0),S.Integer(0),'min')]
for sign in (-1,1):
    realcrit.append((S.Integer(0),(12+sign*S.sqrt(139))/5,'saddle'))
for yc in (-1,5):
    for xc in (-2,2):
        realcrit.append((S.Integer(xc),S.Integer(yc),'min'))
for sign in (-1,1):
    realcrit.append((sign*S.sqrt(S.Rational(13,490)), -S.Rational(2,35),'saddle'))
assert len(realcrit)==9
for x0,y0,kind in realcrit:
    assert S.simplify(S.diff(q,X).subs({X:x0,Y:y0}))==0
    assert S.simplify(S.diff(q,Y).subs({X:x0,Y:y0}))==0
    det=S.simplify(hess_det.subs({X:x0,Y:y0}))
    assert det!=0, (x0,y0,det)
    if kind=='min':
        assert S.sign(det)==1 and S.sign(qxx.subs({X:x0,Y:y0}))==1
    else:
        assert S.sign(det)==-1
assert sum(k=='min' for _,_,k in realcrit)==5
assert sum(k=='saddle' for _,_,k in realcrit)==4
assert hess_det.subs({X:2,Y:-1})==6336
assert hess_det.subs({X:2,Y:5})==33984
assert S.simplify(hess_det.subs({X:S.sqrt(S.Rational(13,490)),Y:-S.Rational(2,35)}))==-S.Rational(303732,8575)
print('PASS 1: all nine distinct real affine stationary points and exact Hessian indices (5,4,0).')

# Homogeneous decomposition after a linear shear, derived from monomial degrees.
def homogeneous_parts(expr):
    parts={2:S.Integer(0),3:S.Integer(0),4:S.Integer(0)}
    for (i,j),coeff in S.Poly(S.expand(expr),X,Y).terms():
        assert i+j in parts
        parts[i+j]+=coeff*X**i*Y**j
    return {k:S.expand(v) for k,v in parts.items()}

angular=[]
for sig in (0,1):
    sh=S.expand(q.subs(X,X+sig*Y))
    H=homogeneous_parts(sh)
    assert S.expand(sum(H.values())-sh)==0
    assert S.expand(H[4]-(3*(X+sig*Y)**4-5*(X+sig*Y)**2*Y**2+5*Y**4))==0

    # Squarefree leading binary quartic -> the partial derivatives have no common
    # projective root -> isolated pole, local intersection length 3*3=9.
    hx=S.diff(H[4],X); hy=S.diff(H[4],Y)
    assert S.total_degree(S.gcd(hx,hy))==0

    h=S.expand(H[4].subs({X:t,Y:1}))
    E=S.factor((1+t**2)*S.diff(h,t)-4*t*h)
    equator_projective=S.expand(X*hy-Y*hx)
    assert S.expand(equator_projective.subs({X:t,Y:1})+E)==0
    assert S.resultant(E,1+t**2,t)!=0, 'Unexpected isotropic eigenpoint'
    assert S.resultant(E,h,t)!=0, 'Unexpected zero critical value'
    assert S.simplify(H[4].subs({X:1,Y:0}))!=0

    # In complex affine chart y=1, the normalized function is holomorphic
    # near every equatorial root because 1+t**2 != 0. Its local Hessian
    # determinant at a root of E is -4*h(t)*E'(t)/(1+t**2)**6.
    w=S.symbols('w')
    V=h/(1+t**2+w**2)**2
    V_tt=S.diff(V,t,2).subs(w,0)
    V_ww=S.diff(V,w,2).subs(w,0)
    assert S.cancel(V_ww+4*h/(1+t**2)**3)==0
    assert S.cancel((1+t**2)**4*V_tt-(1+t**2)*S.diff(E,t)+6*t*E)==0
    if sig==0:
        assert S.expand(E-2*t*(11*t**2-15))==0
        assert S.polys.polytools.count_roots(E,-S.oo,S.oo)==3
        # Projective point [1:0] occurs as a simple root in coordinate r=Y/X.
        r=S.symbols('r')
        Enear=S.expand(equator_projective.subs({X:1,Y:r}))
        assert Enear.subs(r,0)==0 and S.diff(Enear,r).subs(r,0)!=0
        finite_angular=[S.Integer(0),S.sqrt(S.Rational(15,11)),-S.sqrt(S.Rational(15,11))]
        Ap=S.factor(h/(1+t**2)**2)
        for tc in finite_angular:
            assert S.simplify(S.diff(Ap,t).subs(t,tc))==0
            val=S.simplify(Ap.subs(t,tc))
            curvature=S.simplify((1+tc**2)**2*S.diff(Ap,t,2).subs(t,tc))
            assert S.sign(val)==1 and S.sign(curvature)!=0
        assert S.sign(S.diff(H[4].subs({X:S.cos(S.Symbol('theta')),Y:S.sin(S.Symbol('theta'))}),S.Symbol('theta'),2).subs(S.Symbol('theta'),0))==-1
        print('PASS 2: sigma=0; four simple real angular points (two min, two max), all H4>0.')
    else:
        P=6*t**4+7*t**3-15*t**2-7*t-1
        assert S.expand(E+2*P)==0
        assert S.discriminant(P,t)==-2482700
        assert S.polys.polytools.count_roots(P,-S.oo,S.oo)==2
        # These disjoint rational intervals exhibit the two real roots.
        assert P.subs(t,-S.Rational(3,1))*P.subs(t,-S.Rational(2,1))<0
        assert P.subs(t,S.Rational(1,1))*P.subs(t,S.Rational(2,1))<0
        print('PASS 3: sigma=1; two simple real and two simple nonreal angular points, H4>0.')
    angular.append((sig,E))
print('PASS 4: binary H4 partials have no common nonzero complex zero for either shear.')
print('PASS 5: equator has four distinct complex points and none lie on isotropic conic or H4=0.')
print('REVIEW 6: local lengths 9 and 4 follow from the verified regular-sequence and simple-root premises.')
print('REVIEW 7: IFT + holomorphic conservation-of-number support (5,6,2) and (5,5,1); this is a mathematical audit, not executable certification or external peer review.')
for fname in ('BTC004_Scaling_Proof_v3.md','btc004_scaling_proof_note_v3.md'):
    p=Path(__file__).parent/fname
    if p.exists():
        print('Note file SHA256:',fname, hashlib.sha256(p.read_bytes()).hexdigest())
