import numpy as np
from scipy.interpolate import RegularGridInterpolator

# 입력 데이터 설정
x1, x2 = 150, 200
y1, y2 = 0.1, 0.2
z11, z12 = 2582.9, 2577.1
z21, z22 = 2658.2, 2654.6

xi = 160
yi = 0.12

# x, y 좌표축 정의 및 z 데이터 행렬 구성
x = np.array([x1, x2])
y = np.array([y1, y2])
z = np.array([[z11, z21], [z12, z22]]) # interp2d와 인덱싱 구조를 맞추기 위해 전치 필요할 수 있음

# RegularGridInterpolator를 이용한 이중 선형 보간 수행
# points는 (x, y) 순서로 정의
interp_func = RegularGridInterpolator((x, y), z, method='linear')
U = interp_func([xi, yi])

# 결과 출력[cite: 14]
print(f"\nT,P에서의 내부에너지={U[0]:10.5f} KJ/kg")