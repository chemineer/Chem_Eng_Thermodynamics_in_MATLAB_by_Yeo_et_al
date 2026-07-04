import numpy as np

def PHIVMIX_PR(nc, y, Pc, Tc, w, P, T):
    """
    Peng-Robinson 방정식을 이용한 기상 혼합물의 퓨가시티 계수 계산 (파이썬 변환)
    """
    R = 8.3143  # J/mol-K
    
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
        
    ar = np.sqrt(np.outer(a, a))
    
    am = np.sum(np.outer(y, y) * ar)
    bm = np.sum(y * b)
            
    # 2. 파라미터 A, B
    A = am * P / (R * T)**2.0
    B = bm * P / (R * T)
    
    Ak = ar * A / am
    Bk = b * B / bm
    A_sum = np.dot(y, Ak)
    
    # 3. 3차 방정식의 계수 및 근 구하기
    a2 = -(1 - B)
    a1 = (A - 3 * B**2 - 2 * B)
    a0 = -(A * B - B**2 - B**3)
    
    EOS = [1, a2, a1, a0]
    Zt = np.roots(EOS)
    
    # 기체상은 가장 큰 실근을 선택
    real_roots = Zt[np.isreal(Zt)].real
    Z = np.max(real_roots)
    
    # 4. 퓨가시티 계수 계산
    c1 = np.log(Z - B)
    c2 = (Z - 1) / B
    c3 = A / (B * np.sqrt(8))
    c4 = np.log((Z + (1 + np.sqrt(2)) * B) / (Z + (1 - np.sqrt(2)) * B))
    
    phiV = np.exp(-c1 + Bk * c2 - c3 * c4 * (2 * A_sum / A - Bk / B))
    
    return phiV