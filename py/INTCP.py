import numpy as np

def INTCP(T1, T2, P1, P2, A, B, C, D):
    # 기체상수 설정
    R = 8.3143  # J/mol-K
    
    # 온도차항 계산
    dT = T2 - T1
    sT = T2**2 - T1**2
    cT = T2**3 - T1**3
    qT = T2**4 - T1**4
    
    # 엔탈피 변화 적분 (T1 -> T2)[cite: 10]
    dh = A * dT + B * sT / 2.0 + C * cT / 3.0 + D * qT / 4.0
    
    # 엔트로피 변화 적분 (T1 -> T2)[cite: 10]
    # 식: A*ln(T2/T1) + B*dT + C*sT/2 + D*cT/3 - R*ln(P2/P1)[cite: 10]
    ds = A * np.log(T2 / T1) + B * dT + C * sT / 2.0 + D * cT / 3.0 - R * np.log(P2 / P1)
    
    return dh, ds