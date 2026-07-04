import numpy as np

def DELHG_RXN(nc, m, a, b, c, d, TR, HR, GR, T):
    """
    반응계에서 온도 T에서의 표준 엔탈피(delH0) 및 깁스 자유 에너지(delG0) 변화 계산 (파이썬 변환)
    """
    R = 8.3143  # J/mol-K

    # 각 계수 및 HR, GR의 합산 계산
    da = np.sum(np.array(m) * np.array(a))
    db = np.sum(np.array(m) * np.array(b))
    dc = np.sum(np.array(m) * np.array(c))
    dd = np.sum(np.array(m) * np.array(d))
    dH = np.sum(np.array(m) * np.array(HR))
    dG = np.sum(np.array(m) * np.array(GR))

    # 상수 J 계산
    J = dH - da * TR - db * (TR**2) / 2.0 - dc * (TR**3) / 3.0 - dd * (TR**4) / 4.0

    # 상수 W 계산
    W = (dG - J + da * TR * np.log(TR) + db * (TR**2) / 2.0 + 
         dc * (TR**3) / 6.0 + dd * (TR**4) / 12.0) / (R * TR)

    # delH0, delG0 계산[cite: 9]
    delH0 = J + da * T + db * (T**2) / 2.0 + dc * (T**3) / 3.0 + dd * (T**4) / 4.0
    delG0 = J - da * T * np.log(T) - db * (T**2) / 2.0 - dc * (T**3) / 6.0 - dd * (T**4) / 12.0 + W * T * R

    return delH0, delG0