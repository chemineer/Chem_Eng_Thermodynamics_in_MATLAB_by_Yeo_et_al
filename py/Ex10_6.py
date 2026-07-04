import numpy as np
from BP_PR import BP_PR

# 시스템 파라미터 설정
nc = 2
T = 100.0
Pi = 4.119  # 기포점 압력 가정값 (bar)

# 성분별 데이터 초기화
x = np.array([0.5, 0.5])      # 액상 몰분율
yi = np.array([0.958, 0.042]) # 기상 몰분율(가정값)
Pc = np.array([33.94, 46.04]) # 임계압력(bar)
Tc = np.array([126.1, 190.6]) # 임계온도(K)[cite: 12]
w = np.array([0.04, 0.011])   # 이심인자[cite: 12]

# 기포점 압력(bp) 및 기상 조성(y) 계산[cite: 12]
bp, y = BP_PR(nc, Pc, Tc, w, x, T, Pi, yi)

# 기상 조성의 합 계산[cite: 12]
sy = np.sum(y)

# 결과 출력[cite: 12]
print(f'\n기포점 압력= {bp/10.0:10.5f} MPa \n')

for i in range(nc):
    print(f'\n기상몰분율(y {i+1:2.0f})= {y[i]:10.5f} \n')

print(f'\n기상몰분율의 합= {sy:10.5f} \n')