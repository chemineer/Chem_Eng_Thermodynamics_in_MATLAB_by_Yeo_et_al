import numpy as np
from DEPFUN_PR import DEPFUN_PR
from INTCP import INTCP

def DELE_PR(T1, T2, P1, P2, Pc, Tc, w, A, B, C, D):
    R = 8.3143  # J/mol-K
    
    # 초기 및 최종 상태에서의 편차 함수 계산
    Z1, V1, DH1, DS1, DU1, DG1, DA1, Sc1, Ac1 = DEPFUN_PR(P1, T1, Pc, Tc, w)
    Z2, V2, DH2, DS2, DU2, DG2, DA2, Sc2, Ac2 = DEPFUN_PR(P2, T2, Pc, Tc, w)
    
    # 이상기체의 상태 변화 (1-->2)
    delH_ig, delS_ig = INTCP(T1, T2, P1, P2, A, B, C, D)
    
    len_Z1 = 1 if np.isscalar(Z1) else len(Z1)
    len_Z2 = 1 if np.isscalar(Z2) else len(Z2)
    
    # 매트랩 원본의 조건문 로직 복원 (상 개수 변화 완벽 대응)
    if len_Z1 == 1 and len_Z2 == 1:
        DH = DH2 + delH_ig - DH1
        DS = DS2 + delS_ig - DS1
    elif len_Z1 == 1 and len_Z2 != 1:
        DH = np.zeros(len_Z2)
        DS = np.zeros(len_Z2)
        for i in range(len_Z2):
            DH[i] = DH2[i] + delH_ig - DH1
            DS[i] = DS2[i] + delS_ig - DS1
    elif len_Z1 != 1 and len_Z2 == 1:
        for i in range(len_Z1):
            DH = DH2 + delH_ig - DH1[i]
            DS = DS2 + delS_ig - DS1[i]
    else:
        DH = np.zeros(len_Z2)
        DS = np.zeros(len_Z2)
        for i in range(len_Z2):
            DH[i] = DH2[i] + delH_ig - DH1[i]
            DS[i] = DS2[i] + delS_ig - DS1[i]
            
    # 매트랩 원본 수식으로 복원 (결정적 차이 해결!)
    DU = DH - Z2 * R * T2
    
    return Z1, Z2, DU, DH, DS