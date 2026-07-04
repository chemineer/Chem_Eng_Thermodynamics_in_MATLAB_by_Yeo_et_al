import numpy as np
from PHILMIX_PR import PHILMIX_PR
from PHIVMIX_PR import PHIVMIX_PR

# 시스템 파라미터 설정
nc = 2
T = 100.0
P = 4.119

# 성분별 데이터 초기화
x = np.array([0.5, 0.5])      # 액상 몰분율
y = np.array([0.958, 0.042])  # 기상 몰분율(가정값)
Pc = np.array([33.94, 46.04]) # 임계압력(bar)[cite: 11]
Tc = np.array([126.1, 190.6]) # 임계온도(K)[cite: 11]
w = np.array([0.04, 0.011])   # 이심인자[cite: 11]

# 혼합물의 푸가시티 계수 계산[cite: 11]
# PHILMIX_PR과 PHIVMIX_PR은 사용자의 환경에 맞게 구현되어 있어야 합니다.
phiL = PHILMIX_PR(nc, x, Pc, Tc, w, P, T)
phiV = PHIVMIX_PR(nc, y, Pc, Tc, w, P, T)

# K값 계산 및 기상 몰분율 업데이트[cite: 11]
K = np.zeros(nc)
for i in range(nc):
    K[i] = phiL[i] / phiV[i]

sumy = 0.0
for i in range(nc):
    y[i] = K[i] * x[i]
    sumy += y[i]

# 결과 출력[cite: 11]
for i in range(nc):
    print(f'액상의 fugacity계수 (성분 {i+1:2.0f}) : {phiL[i]:11.5f}')
    print(f'기상의 fugacity계수 (성분 {i+1:2.0f}) : {phiV[i]:11.5f}')
    print(f'K value (성분 {i+1:2.0f}) : {K[i]:11.5f}')
    print(f'기상의 몰분율 (성분 {i+1:2.0f}) : {y[i]:11.5f}')

print(f'기상 몰분율의 합 : {sumy:11.5f}')