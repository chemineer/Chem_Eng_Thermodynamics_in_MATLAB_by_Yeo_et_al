import numpy as np
from DELHG_RXN import DELHG_RXN

R = 8.3143  # J/mol-K
nc = 3      # 성분수

# 각 성분별 데이터 배열 초기화
m = np.array([-1, -1, 1])
a = np.array([3.806, 32.24, 9.014])
b = np.array([1.566e-1, 1.924e-3, 2.141e-1])
c = np.array([-8.348e-5, 1.055e-5, -8.39e-5])
d = np.array([1.755e-8, -3.596e-9, 1.373e-9])
HR = np.array([52.51, -241.835, -234.95])    # kJ/mol
GR = np.array([68.43, -228.614, -167.73])    # kJ/mol

TR = 298.15     # 기준온도(K)
T_degC = 145    # 반응온도(deg C)

# kJ/mol을 J/mol로 변환
HR = HR * 1000.0
GR = GR * 1000.0

# 섭씨를 켈빈으로 변환
T = T_degC + 273.15

# delH0 and delG0 at T 계산 (외부 함수 호출)
delH0, delG0 = DELHG_RXN(nc, m, a, b, c, d, TR, HR, GR, T)

# 평형상수 K 계산[cite: 13]
K = np.exp(-delG0 / (R * T))

# 결과 출력[cite: 13]
print(f'del H0 at {T-273.15:8.3f} deg C = {delH0:10.5f} J/mol')
print(f'del G0 at {T-273.15:8.3f} deg C = {delG0:10.5f} J/mol')
print(f'평형상수 K at {T-273.15:8.3f} deg C = {K:10.5f}')