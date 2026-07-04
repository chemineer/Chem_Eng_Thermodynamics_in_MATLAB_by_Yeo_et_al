import numpy as np

# PRPURE_V 함수가 동일한 스크립트나 모듈에 정의되어 있어야 합니다
from PRPURE_V import PRPURE_V


# 데이터 설정
data = np.array([150.86, 4.898, -0.004])  # [Tc(K), Pc(MPa), w]
cond = np.array([105.6, 0.498])          # [T(K), P(MPa)]

# 몰 부피 계산
Vol = PRPURE_V(data, cond)
Z = np.array([Vol[0], Vol[1], Vol[2]])

# 결과 출력
print(f"\n Z values : {Z}")
print("\n몰 부피(Molar volume) :")
print(f"\n   Vapor = {Vol[3]:10.5f} cm^3/mol")
print(f"   Liquid = {Vol[4]:10.5f} cm^3/mol")

