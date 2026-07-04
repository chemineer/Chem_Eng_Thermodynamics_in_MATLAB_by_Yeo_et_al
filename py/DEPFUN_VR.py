def DEPFUN_VR(P, T, Pc, Tc, w):
    """
    Virial 상태 방정식을 이용한 편차 함수 DH, DS 계산 (파이썬 변환)
    """
    # 기체상수
    R = 8.3143  # J/mol-K

    # 환산 온도(Tr) 및 환산 압력(Pr) 계산
    Tr = T / Tc
    Pr = P / Pc

    # 상태 방정식 파라미터 계산[cite: 12]
    c1 = 1.0972 / (Tr**2.6) - 0.083 / Tr
    c2 = 0.8944 / (Tr**5.2) - 0.139 / Tr
    c3 = 0.675 / (Tr**2.6)
    c4 = 0.722 / (Tr**5.2)

    # 편차 함수 DH, DS 계산[cite: 12]
    DH = -R * T * Pr * (c1 + w * c2)
    DS = -R * Pr * (c3 + w * c4)

    return DH, DS