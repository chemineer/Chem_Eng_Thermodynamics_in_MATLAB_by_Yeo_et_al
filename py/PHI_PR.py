import numpy as np

def PHI_PR(P, T, Pc, Tc, w):
    """
    Peng-Robinson 방정식을 이용한 퓨가시티 계수 및 퓨가시티 계산 (파이썬 변환)
    """
    R = 8.3143  # J/mol-K

    Tr = T / Tc  # 환산 온도
    
    # 방정식 파라미터 계산
    k = 0.37464 + 1.54226 * w - 0.26993 * w**2.0
    alpha = (1.0 + k * (1.0 - np.sqrt(Tr)))**2.0
    ac = 0.45723553 * (R**2 * Tc**2.0) / Pc
    a = ac * alpha
    b = 0.07779607 * R * Tc / Pc

    A = (a * P) / (R**2 * T**2.0)
    B = (b * P) / (R * T)

    # 3차 방정식 계수[cite: 14]
    a2 = -(1.0 - B)
    a1 = (A - 3.0 * B**2 - 2.0 * B)
    a0 = -(A * B - B**2 - B**3)

    # 3차 방정식의 근 계산[cite: 14]
    EOS = [1.0, a2, a1, a0]
    Zt = np.roots(EOS)
    
    # 실근만 선택[cite: 14]
    Zr = Zt[np.isreal(Zt)].real 
    
    if len(Zr) == 3:
        Z = np.array([np.min(Zr), np.max(Zr)])  # [액체근, 기체근][cite: 14]
    else:
        Z = np.array([Zr[0]])

    # 퓨가시티 및 퓨가시티 계수 계산[cite: 14]
    c1 = np.log((Z + (1.0 + np.sqrt(2.0)) * B) / (Z + (1.0 - np.sqrt(2.0)) * B))
    c2 = A / (B * np.sqrt(8.0))

    phi = np.exp(Z - 1.0 - np.log(Z - B) - c2 * c1)
    f = phi * P

    return phi, f