import numpy as np
from DELHS_PR import DELHS_PR  # 별도 파일에서 함수 가져오기

# 초기 데이터 설정
Tc = 369.8
Pc = 42.49
w = 0.152

A = -4.224
B = 0.3063
C = -1.586e-4
D = 3.215e-8

T1 = 378.15
P1 = 5
T2 = 463.15
P2 = 25

# 1->2에서 엔탈피 및 엔트로피 변화 계산
Z1, Z2, DH, DS = DELHS_PR(T1, T2, P1, P2, Pc, Tc, w, A, B, C, D)

# 결과 출력
print('\n엔탈피 및 엔트로피 변화')
if len(Z2) == 1:
    print(f'\n Z2={Z2[0]:10.7f} \n DH={DH[0]:10.4f} J/mol\n DS={DS[0]:10.4f} J/mol-K')
else:
    for i in range(len(Z2)):
        print(f'\n Z2({i+1})={Z2[i]:10.7f} \n DH={DH[i]:10.4f} J/mol\n DS={DS[i]:10.4f} J/mol-K')