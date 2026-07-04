import numpy as np
from VMIX_VR import VMIX_VR

# 성분수 설정
nc = 2

# 데이터 배열 초기화
Tc = np.zeros(nc)
Pc = np.zeros(nc)
Vc = np.zeros(nc)
Zc = np.zeros(nc)
w = np.zeros(nc)
x = np.zeros(nc)

# 1번 성분 데이터
Tc[0], Pc[0], Vc[0], Zc[0], w[0], x[0] = 433.8, 31.99, 303.28, 0.269, 0.196, 0.6

# 2번 성분 데이터
Tc[1], Pc[1], Vc[1], Zc[1], w[1], x[1] = 304.2, 73.82, 93.87, 0.274, 0.228, 0.4

# 시스템 조건[cite: 10]
T = 310
P = 2

# 혼합물의 부피 계산[cite: 10]
V = VMIX_VR(nc, Tc, Pc, Vc, Zc, w, x, T, P)

# 결과 출력[cite: 10]
print(f"\n혼합물의 부피 = {V:11.5f} cm^3/mol \n")