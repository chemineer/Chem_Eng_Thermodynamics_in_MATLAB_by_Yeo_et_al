import numpy as np

def DEPFUN_PR(P, T, Pc, Tc, w):
    # 기체 상수 설정
    R = 8.3143    # J/mol-K
    Rv = 83.143   # bar-cm^3/mol-K

    Tr = T / Tc   # 환산 온도
    Pr = P / Pc   # 환산 압력

    # 방정식 파라미터 계산
    k = 0.37464 + 1.54226 * w - 0.26993 * w**2
    alpha = (1 + k * (1 - np.sqrt(Tr)))**2
    ac = 0.45723553 * (R**2 * Tc**2) / Pc
    a = ac * alpha
    b = 0.07779607 * R * Tc / Pc

    A = (a * P) / (R**2 * T**2)
    B = (b * P) / (R * T)

    # 3차 방정식 계수
    a2 = -(1 - B)
    a1 = (A - 3 * B**2 - 2 * B)
    a0 = -(A * B - B**2 - B**3)

    # 3차 방정식의 실근 선택
    EOS = [1, a2, a1, a0]
    Zt = np.roots(EOS)
    real_mask = np.isclose(Zt.imag, 0, atol=1e-9)
    Zr = Zt[real_mask].real

    if len(Zr) == 3: # 3개의 실근인 경우
        Z = np.array([np.min(Zr), np.max(Zr)])
    else:
        Z = np.array([Zr[0]])

    # 부피 계산
    V = Z * Rv * T / P

    # 편차 함수 계산
    c1 = np.log((Z + (1 + np.sqrt(2)) * B) / (Z + (1 - np.sqrt(2)) * B))
    c2 = A / (B * np.sqrt(8))
    c3 = k * np.sqrt(Tr / alpha)
    c4 = np.log((Z - B) / Z)

    DH = R * T * (Z - 1 - c2 * (1 + c3) * c1)
    DU = R * T * (-c2 * (1 + c3) * c1)
    DS = R * (np.log(Z - B) - c2 * c3 * c1)
    DG = R * T * (Z - 1 - np.log(Z - B) - c2 * c1)
    DA = R * T * (-np.log(Z - B) - c2 * c1)
    DA_TV = R * T * (-c4 - c2 * c1)
    DS_TV = R * (c4 - c2 * c3 * c1)

    return Z, V, DH, DS, DU, DG, DA, DS_TV, DA_TV