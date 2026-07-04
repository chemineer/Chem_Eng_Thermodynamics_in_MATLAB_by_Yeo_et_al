import numpy as np
from PHILMIX_PR import PHILMIX_PR
from PHIVMIX_PR import PHIVMIX_PR

def BPfun(nc, Pc, Tc, w, x, yi, T, P):
    """
    Peng-Robinson 방정식을 이용한 기포점 압력 계산 중 sum(y_i)-1 계산 (파이썬 변환)
    """
    eps = 1.0e-5
    
    # 퓨가시티 계수 계산 (외부 함수 필요)
    # phiL, phiV는 각 성분에 대한 배열 형태여야 함
    phiL = PHILMIX_PR(nc, x, Pc, Tc, w, P, T)
    phiV = PHIVMIX_PR(nc, yi, Pc, Tc, w, P, T)
    
    # 초기 y(i) 계산
    K = phiL / phiV
    y = K * np.array(x)
    
    y_old = 0.0
    y_new = 2.0
    
    # y의 합이 수렴할 때까지 반복
    while abs(y_new - y_old) > eps:
        y_old = y_new
        phiV = PHIVMIX_PR(nc, y, Pc, Tc, w, P, T)
        
        # K(i) 및 y(i) 재계산
        K = phiL / phiV
        y = K * np.array(x)
        
        # 기상 몰분율의 합 계산
        y_new = np.sum(y)
        
        # y(i) 정규화
        y = y / y_new
        
    f = y_new - 1.0
    
    return f, y