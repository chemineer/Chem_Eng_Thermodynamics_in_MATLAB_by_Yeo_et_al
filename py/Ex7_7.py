import numpy as np
from DELHS_PR import DELHS_PR  # 별도 정의된 DELHS_PR 함수 호출

# 물성 데이터 설정
Tc = 190.6    # 임계온도(K)
Pc = 45.99    # 임계압력(bar)
w = 0.012     # 이심인자[cite: 6]

A = 19.25     # Cp data(A)[cite: 6]
B = 0.0523    # Cp data(B)[cite: 6]
C = 1.197e-5  # Cp data(C)[cite: 6]
D = -1.132e-8 # Cp data(D)[cite: 6]

# 기준 및 상태 조건 설정[cite: 6]
T0, P0 = 300, 60
T6, P6 = 111, 1.013
T8, P8 = 295, 1.013

# 엔탈피 및 엔트로피 계산[cite: 6]
Z0_6, Z6, H6, S6 = DELHS_PR(T0, T6, P0, P6, Pc, Tc, w, A, B, C, D)
Z0_8, Z8, H8, S8 = DELHS_PR(T0, T8, P0, P8, Pc, Tc, w, A, B, C, D)

# 상태 6 결과 출력[cite: 6]
print('\n--- 상태 6 ---')
if len(Z6) == 1:
    print(f' Z={Z6[0]:10.7f} \n H6={H6[0]:10.4f} J/mol\n S6={S6[0]:10.4f} J/mol-K')
else:
    for i in range(len(Z6)):
        print(f' Z={Z6[i]:10.7f} \n H6={H6[i]:10.4f} J/mol\n S6={S6[i]:10.4f} J/mol-K')

# 상태 8 결과 출력[cite: 6]
print('\n--- 상태 8 ---')
if len(Z8) == 1:
    print(f' Z={Z8[0]:10.7f} \n H8={H8[0]:10.4f} J/mol\n S8={S8[0]:10.4f} J/mol-K')
else:
    for i in range(len(Z8)):
        print(f' Z={Z8[i]:10.7f} \n H8={H8[i]:10.4f} J/mol\n S8={S8[i]:10.4f} J/mol-K')

# 액화된 분율 계산 및 출력[cite: 6]
# H6가 배열인 경우 첫 번째 원소를 사용[cite: 6]
frL = -H8[0] / (H6[0] - H8[0])
print(f'\n액화된 분율 {frL:10.5f}')