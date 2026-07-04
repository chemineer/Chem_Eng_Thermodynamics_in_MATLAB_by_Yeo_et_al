import numpy as np

def PRPURE_V(dat, cond):
    # dat: [Tc, Pc, w]
    # cond: [T, P]
    # 반환: [Z1, Z2, Z3, V_vapor, V_liquid]
    
    Tc, Pc, w = dat[0], dat[1], dat[2]
    T, P = cond[0], cond[1]
    
    R = 8.314  # 이상기체 상수 (cm^3-MPa/mol-K)
    Tr = T / Tc
    Pr = P / Pc
    
    # 파라미터 계산
    k = 0.37464 + 1.54226 * w - 0.26993 * w**2
    alpha = (1 + k * (1 - np.sqrt(Tr)))**2
    ac = 0.45723553 * (R**2 * Tc**2) / Pc
    a = ac * alpha
    b = 0.07779607 * R * Tc / Pc
    
    A = (a * P) / (R**2 * T**2)
    B = (b * P) / (R * T)
    
    # 3차 방정식의 계수: Z^3 + a2*Z^2 + a1*Z + a0 = 0
    a3 = 1.0
    a2 = -(1 - B)
    a1 = (A - 3 * B**2 - 2 * B)
    a0 = -(A * B - B**2 - B**3)
    
    # 3차 방정식 풀이[cite: 3]
    p = [a3, a2, a1, a0]
    Z = np.roots(p)
    
    V = np.zeros(5)
    V[0:3] = Z
    
    # 몰 부피 계산[cite: 3]
    vapz = 0.0
    liqz = 2.0
    
    for i in range(3):
        realz = np.real(Z[i])
        if abs(np.imag(Z[i])) < 1.0e-9:
            if realz > vapz:
                vapz = realz
            elif realz < vapz and realz < liqz:
                liqz = realz
                
    # 증기 몰 부피[cite: 3]
    if vapz > 0.0:
        V[3] = vapz * R * T / P
    else:
        V[3] = 0.0
        
    # 액상 몰 부피[cite: 3]
    if liqz < 1.0:
        V[4] = liqz * R * T / P
    else:
        V[4] = 0.0
        
    return V