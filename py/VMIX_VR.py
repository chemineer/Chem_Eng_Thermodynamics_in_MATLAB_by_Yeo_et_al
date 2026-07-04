import numpy as np

def VMIX_VR(nc, Tc, Pc, Vc, Zc, w, x, T, P):
    """
    Virial 상태 방정식을 이용한 혼합물의 부피 계산 (파이썬 변환)
    """
    R = 83.143  # bar-cm^3/mol-K

    # 혼합물의 임계 properties 계산
    Tcm = np.zeros((nc, nc))
    Vcm = np.zeros((nc, nc))
    Zcm = np.zeros((nc, nc))
    wm = np.zeros((nc, nc))
    Pcm = np.zeros((nc, nc))
    Trm = np.zeros((nc, nc))

    for i in range(nc):
        for j in range(nc):
            Tcm[i, j] = np.sqrt(Tc[i] * Tc[j])
            Vcm[i, j] = ((Vc[i]**(1/3) + Vc[j]**(1/3)) / 2)**3
            Zcm[i, j] = (Zc[i] + Zc[j]) / 2
            wm[i, j] = (w[i] + w[j]) / 2
            Pcm[i, j] = Zcm[i, j] * R * T / Vcm[i, j]
            Trm[i, j] = T / Tcm[i, j]

    # 혼합물의 virial parameters 계산
    Bm = np.zeros((nc, nc))
    for i in range(nc):
        for j in range(nc):
            B0 = 0.083 - 0.422 / (Trm[i, j]**1.6)
            B1 = 0.139 - 0.172 / (Trm[i, j]**4.2)
            Bm[i, j] = (B0 + wm[i, j] * B1) * R * Tcm[i, j] / Pcm[i, j]

    # 혼합물에 대한 B 계산
    B_mix = 0
    for i in range(nc):
        for j in range(nc):
            B_mix += x[i] * x[j] * Bm[i, j]

    # 혼합물의 부피 계산
    Z = 1 + B_mix * P / (R * T)
    V = Z * R * T / P

    return V