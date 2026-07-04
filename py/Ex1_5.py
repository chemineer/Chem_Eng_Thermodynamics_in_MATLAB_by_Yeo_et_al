import numpy as np
from dblinterp import dblinterp

# 데이터 정의[cite: 13]
x = np.array([200, 250])
y = np.array([1.0, 1.2])

z1 = np.array([[2622.2, 2612.9], [2710.4, 2704.7]]) # 내부에너지 행렬[cite: 13]
z2 = np.array([[0.2060, 0.1693], [0.2327, 0.1924]])  # 부피 행렬[cite: 13]

z_target = 2650
v_target = 0.185
w = [z_target, v_target]

# 함수 호출[cite: 13]
s = dblinterp(x, y, z1, z2, w)

# 결과 출력[cite: 13]
print(f"\n온도={s[0]:10.5f} deg.C")
print(f"압력={s[1]:10.5f} MPa")