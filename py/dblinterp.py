import numpy as np

def dblinterp(x, y, z1, z2, w):
    """
    이중 선형 보간을 사용하여 두 종속 변수 값을 계산 (파이썬 변환)
    """
    x1, x2 = x[0], x[1]
    y1, y2 = y[0], y[1]
    dx = x2 - x1
    dy = y2 - y1

    z11, z12 = z1[0, 0], z1[0, 1]
    z21, z22 = z1[1, 0], z1[1, 1]
    z = w[0]

    v11, v12 = z2[0, 0], z2[0, 1]
    v21, v22 = z2[1, 0], z2[1, 1]
    v = w[1]

    # z1(예: 엔탈피)에 대한 계수 계산
    dz = z11 + z22 - z12 - z21
    dz1 = z12 - z11
    dz2 = z21 - z11
    a1 = dz / (dx * dy)
    b1 = dz2 / dx - y1 * dz / (dx * dy)
    c1 = dz1 / dy - x1 * dz / (dx * dy)
    d1 = z11 - x1 * dz2 / dx - y1 * dz1 / dy + x1 * y1 * dz / (dx * dy) - z

    # z2(예: 부피)에 대한 계수 계산
    dv = v11 + v22 - v12 - v21
    dv1 = v12 - v11
    dv2 = v21 - v11
    a2 = dv / (dx * dy)
    b2 = dv2 / dx - y1 * dv / (dx * dy)
    c2 = dv1 / dy - x1 * dv / (dx * dy)
    d2 = v11 - x1 * dv2 / dx - y1 * dv1 / dy + x1 * y1 * dv / (dx * dy) - v

    # 이차 방정식의 계수 A, B, C 계산
    A = a1 * b2 - a2 * b1
    B = a1 * d2 - a2 * d1 + c1 * b2 - c2 * b1
    C = c1 * d2 - c2 * d1

    # 근의 공식 적용
    s1 = (-B + np.sqrt(B**2 - 4.0 * A * C)) / (2.0 * A)
    s2 = (-b1 * s1 - d1) / (a1 * s1 + c1)
    
    return np.array([s1, s2])