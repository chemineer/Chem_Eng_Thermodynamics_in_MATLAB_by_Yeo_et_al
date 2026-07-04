import numpy as np
from PHI_PR import PHI_PR

# 파라미터 설정
Tc, Pc, w = 190.6, 46.04, 0.011
P = 1.0  # bar
eps = 1.0e-5

# 초기 온도 탐색
x1 = 150.0
p1, f1 = PHI_PR(P, x1, Pc, Tc, w)
while len(p1) != 2:
    x1 += 10.0
    p1, f1 = PHI_PR(P, x1, Pc, Tc, w)

x2 = 50.0
p2, f2 = PHI_PR(P, x2, Pc, Tc, w)
while len(p2) != 2:
    x2 += 10.0
    p2, f2 = PHI_PR(P, x2, Pc, Tc, w)

# 이분법(Bisection method) 반복 계산
T = (x1 + x2) / 2.0
while abs(x2 - x1) > eps:
    p1, f1 = PHI_PR(P, x1, Pc, Tc, w)
    p2, f2 = PHI_PR(P, x2, Pc, Tc, w)
    T = (x1 + x2) / 2.0
    pT, f = PHI_PR(P, T, Pc, Tc, w)
    
    # 두 상의 푸가시티 계수 차이를 이용한 수렴 판단
    if (p1[0] - p1[1]) * (pT[0] - pT[1]) > 0:
        x1 = T
    else:
        x2 = T

# 결과 출력
print(f"\n온도={T:10.5f} K")
print(f"Fugacity계수={pT[0]:10.5f}")
print(f"Fugacity(액상)={f[0]/10.0:10.5f} MPa")
print(f"Fugacity(기상)={f[1]/10.0:10.5f} MPa")