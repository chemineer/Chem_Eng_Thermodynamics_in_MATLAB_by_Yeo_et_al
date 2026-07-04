import numpy as np
from DELE_PR import DELE_PR

# 상수 설정
R = 8.3143  # J/mol-K
Tc = 369.8
Pc = 42.49
w = 0.152

A, B, C, D = -4.224, 0.3063, -1.586e-4, 3.215e-8

T0, P0 = 298.0, 0.1 * 10.0  # MPa -> bar
T1, P1 = 350.0, 1.0 * 10.0
P2 = 1.0 * 10.0

# 초기 상태 계산
Z0_init, Z1_init, U1_init, H1_init, S1_init = DELE_PR(T0, T1, P0, P1, Pc, Tc, w, A, B, C, D)

# 초기 상태 출력 (스칼라/배열 판별 복원)
def print_results(label, Z, U, H, S):
    if np.isscalar(Z):
        print(f"\n {label}={Z:10.7f}")
        print(f" U={U:10.4f}, H={H:10.4f}, S={S:10.4f}")
    else:
        for i, z_val in enumerate(Z):
            print(f"\n {label}({i+1})={z_val:10.7f}")
            print(f" U={U[i]:10.4f} J/mol\n H={H[i]:10.4f} J/mol\n S={S[i]:10.4f} J/mol-K")

print_results("Z1", Z1_init, U1_init, H1_init, S1_init)

# 반복 계산을 위한 초기화
Uf = H1_init
eps = 1.0e-5

# 구간 찾기 (매트랩의 배열 조건 비교 방식 적용)
x1 = 355.0
_, _, U_x1, _, _ = DELE_PR(T0, x1, P0, P1, Pc, Tc, w, A, B, C, D)
while np.any(U_x1 - Uf > 0):
    x1 -= 5.0
    _, _, U_x1, _, _ = DELE_PR(T0, x1, P0, P1, Pc, Tc, w, A, B, C, D)

x2 = 400.0
_, _, U_x2, _, _ = DELE_PR(T0, x2, P0, P1, Pc, Tc, w, A, B, C, D)
while np.any(U_x2 - Uf < 0):
    x2 -= 5.0
    _, _, U_x2, _, _ = DELE_PR(T0, x2, P0, P1, Pc, Tc, w, A, B, C, D)

# 이분법 (Bisection method)
while abs(x2 - x1) > eps:
    _, _, U1, _, _ = DELE_PR(T0, x1, P0, P1, Pc, Tc, w, A, B, C, D)
    x = (x1 + x2) / 2.0
    _, _, U, _, _ = DELE_PR(T0, x, P0, P1, Pc, Tc, w, A, B, C, D)
    
    if np.any((U1 - Uf) * (U - Uf) < 0):
        x2 = x
    else:
        x1 = x

# 최종 상태 계산
T2 = x
print(f"\n최종온도={T2:10.5f} (K)\n")
Z0_final, Z2_final, U2_final, H2_final, S2_final = DELE_PR(T0, T2, P0, P2, Pc, Tc, w, A, B, C, D)

print_results("Z2", Z2_final, U2_final, H2_final, S2_final)