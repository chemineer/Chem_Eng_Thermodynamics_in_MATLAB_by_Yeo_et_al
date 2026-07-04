import numpy as np
# DELHS_PR 함수가 정의된 모듈을 import 합니다
from DELHS_PR import DELHS_PR

# 데이터 설정
Tc = 369.8      # 임계온도(K)[cite: 5]
Pc = 4.249      # 임계압력(MPa)[cite: 5]
w = 0.152       # 이심인자[cite: 5]

A = -4.224      # Cp data(A)[cite: 5]
B = 0.3063      # Cp data(B)[cite: 5]
C = -1.586e-4   # Cp data(C)[cite: 5]
D = 3.215e-8    # Cp data(D)[cite: 5]

T1 = 105 + 273.15   # 초기온도(K)[cite: 5]
P1 = 5              # 초기압력(bar)[cite: 5]
T2 = 190 + 273.15   # 최종온도(K)[cite: 5]
P2 = 25             # 최종압력(bar)[cite: 5]

# 단위 변환[cite: 5]
Pc = Pc * 10        # MPa에서 bar로 변환[cite: 5]

# 1->2에서 엔탈피 및 엔트로피 변화 계산[cite: 5]
Z1, Z2, DH, DS = DELHS_PR(T1, T2, P1, P2, Pc, Tc, w, A, B, C, D)

# 결과 출력[cite: 5]
print(f'\n엔탈피 변화(1-->2) : {DH[0]:10.5f} J/mol')
print(f'엔트로피 변화(1-->2) : {DS[0]:10.5f} J/mol-K')