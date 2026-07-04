import numpy as np
# DELHS_VR 함수가 정의된 모듈을 import 합니다.
from DELHS_VR import DELHS_VR 

# 데이터 설정
Tc = 190.6    # 임계온도(K)
Pc = 45.99    # 임계압력(bar)
w = 0.012     # 이심인자[cite: 4]

A = 19.25     # Cp data(A)[cite: 4]
B = 0.0523    # Cp data(B)[cite: 4]
C = 1.197e-5  # Cp data(C)[cite: 4]
D = -1.132e-8 # Cp data(D)[cite: 4]

T1 = 40 + 273.15  # 초기온도(K)[cite: 4]
P1 = 20           # 초기압력(bar)[cite: 4]
P2 = 1            # 최종압력(bar)[cite: 4]

eps = 1.0e-5
x1 = 308.15

# x1 초기 탐색[cite: 4]
f1, s1 = DELHS_VR(T1, x1, P1, P2, Pc, Tc, w, A, B, C, D)
while f1 < 0:
    x1 = x1 + 5.0
    f1, s1 = DELHS_VR(T1, x1, P1, P2, Pc, Tc, w, A, B, C, D)

# x2 초기 탐색[cite: 4]
x2 = 303.15
f2, s2 = DELHS_VR(T1, x2, P1, P2, Pc, Tc, w, A, B, C, D)
while f2 > 0:
    x2 = x2 - 5.0
    f2, s2 = DELHS_VR(T1, x2, P1, P2, Pc, Tc, w, A, B, C, D)

# half-interval 방법을 이용한 반복계산[cite: 4]
while abs(x2 - x1) > eps:
    f1, s1 = DELHS_VR(T1, x1, P1, P2, Pc, Tc, w, A, B, C, D)
    f2, s2 = DELHS_VR(T1, x2, P1, P2, Pc, Tc, w, A, B, C, D)
    x = (x1 + x2) / 2.0
    f, s = DELHS_VR(T1, x, P1, P2, Pc, Tc, w, A, B, C, D)
    
    if f1 * f < 0:
        x2 = x
    else:
        x1 = x

# 결과 출력[cite: 4]
print(f'\n 최종온도= {x - 273.15:10.5f} (deg C) ')