import numpy as np
from PRPURE_V import PRPURE_V

# 데이터 설정
MW = 44
data = np.zeros(3)
data[0] = 304.2     # 임계온도(K)[cite: 2]
data[1] = 73.82     # 임계압력(bar)[cite: 2]
data[2] = 0.228     # 이심인자[cite: 2]

data[1] = data[1] / 10.0  # 임계압력(bar -> MPa)[cite: 2]

cond = np.zeros(2)
cond[0] = 310       # 온도(K)[cite: 2]

# (a) 압력 8 bar 계산[cite: 2]
cond[1] = 8 / 10.0  # 압력(bar -> MPa)[cite: 2]

results = PRPURE_V(data, cond)
Z = np.array([results[0], results[1], results[2]])
results[3] = results[3] / MW # cm^3/gr 변환[cite: 2]
results[4] = results[4] / MW # cm^3/gr 변환[cite: 2]

print(f'\n Z values : {Z}')
print('비 부피(specific volume) :')
print(f'\n   Vapor = {results[3]:10.5f} cm^3/gr')
print(f'   Liquid = {results[4]:10.5f} cm^3/gr')

# (b) 압력 75 bar 계산[cite: 2]
cond[1] = 75 / 10.0 # 압력(bar -> MPa)[cite: 2]

results = PRPURE_V(data, cond)
Z = np.array([results[0], results[1], results[2]])
results[3] = results[3] / MW # cm^3/gr 변환[cite: 2]
results[4] = results[4] / MW # cm^3/gr 변환[cite: 2]

print(f'\n Z values : {Z}')
print('비 부피(specific volume) :')
print(f'\n   Vapor = {results[3]:10.5f} cm^3/gr')
print(f'   Liquid = {results[4]:10.5f} cm^3/gr')