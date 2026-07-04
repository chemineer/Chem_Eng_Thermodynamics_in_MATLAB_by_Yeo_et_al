import numpy as np

def PHILMIX_PR(nc, x, Pc, Tc, w, P, T):
    """
    Peng-Robinson 방정식을 이용한 액상 혼합물의 퓨가시티 계수 계산 (파이썬 변환)
    """
    R = 8.3143  # J/mol-K, 단, 압력 단위가 bar이므로 단위 보정이 필요할 수 있음
    
    # 1. 방정식 파라미터 계산
    a = np.zeros(nc)
    b = np.zeros(nc)
    for i in range(nc):
        Tr = T / Tc[i]
        k = 0.37464 + 1.54226 * w[i] - 0.26993 * w[i]**2.0
        alpha = (1 + k * (1 - np.sqrt(Tr)))**2.0
        ac = 0.45723553 * (R**2 * Tc[i]**2.0) / Pc[i]
        a[i] = ac * alpha
        b[i] = 0.07779607 * R * Tc[i] / Pc[i]
        
    ar = np.zeros((nc, nc))
    for i in range(nc):
        for j in range(nc):
            ar[i, j] = np.sqrt(a[i] * a[j])
            
    am = 0.0
    bm = 0.0
    for i in range(nc):
        bm += x[i] * b[i]
        for j in range(nc):
            am += x[i] * x[j] * ar[i, j]
            
    # 2. 파라미터 A, B
    A = am * P / (R * T)**2.0
    B = bm * P / (R * T)
    
    Ak = ar * A / am
    Bk = b * B / bm
    
    A_sum = np.dot(x, Ak)
    
    # 3. 3차 방정식 계수 및 근 구하기
    a2 = -(1 - B)
    a1 = (A - 3 * B**2 - 2 * B)
    a0 = -(A * B - B**2 - B**3)
    
    EOS = [1, a2, a1, a0]
    Zt = np.roots(EOS)
    
    # 실근 선택 (액체상 조건: 가장 작은 실근)
    real_roots = Zt[np.isreal(Zt)].real
    Z = np.min(real_roots)
    
    # 4. 퓨가시티 계수 계산
    c1 = np.log(Z - B)
    c2 = (Z - 1) / B
    c3 = A / (B * np.sqrt(8))
    c4 = np.log((Z + (1 + np.sqrt(2)) * B) / (Z + (1 - np.sqrt(2)) * B))
    
    phiL = np.exp(-c1 + Bk * c2 - c3 * c4 * (2 * A_sum / A - Bk / B))
    
    return phiL