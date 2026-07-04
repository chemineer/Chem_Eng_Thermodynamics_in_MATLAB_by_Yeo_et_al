import numpy as np
from BPfun import BPfun

def BP_PR(nc, Pc, Tc, w, x, T, Pi, yi):
    """
    Peng-Robinson 방정식을 이용한 기포점 압력 계산 (파이썬 변환)
    """
    eps = 1.0e-5
    delP = 0.5
    
    P1 = Pi
    # f1: 함수값, y1: 기상 몰분율
    # BPfun은 외부에서 정의되어야 함
    f1, y1 = BPfun(nc, Pc, Tc, w, x, yi, T, P1)
    
    while f1 < 0:
        P1 = P1 - delP
        f1, y1 = BPfun(nc, Pc, Tc, w, x, yi, T, P1)
        
    P2 = Pi + delP
    f2, y2 = BPfun(nc, Pc, Tc, w, x, yi, T, P2)
    
    while f2 > 0:
        P2 = P2 + delP
        f2, y2 = BPfun(nc, Pc, Tc, w, x, yi, T, P2)
        
    # 이분법(half-interval method)을 이용한 반복계산
    bp = P1
    y = y1
    
    while abs(P2 - P1) > eps:
        f1, y1 = BPfun(nc, Pc, Tc, w, x, yi, T, P1)
        f2, y2 = BPfun(nc, Pc, Tc, w, x, yi, T, P2)
        
        bp = (P1 + P2) / 2.0
        y = (y1 + y2) / 2.0
        
        f, y = BPfun(nc, Pc, Tc, w, x, y, T, bp)
        
        if f1 * f < 0:
            P2 = bp
        else:
            P1 = bp
            
    return bp, y

# 참고: BPfun 함수는 별도로 구현되어야 합니다.
# def BPfun(nc, Pc, Tc, w, x, yi, T, P):
#     ...
#     return f, y