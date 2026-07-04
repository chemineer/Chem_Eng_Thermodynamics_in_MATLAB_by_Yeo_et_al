import numpy as np
from DEPFUN_VR import DEPFUN_VR
from INTCP import INTCP

def DELHS_VR(T1, T2, P1, P2, Pc, Tc, w, A, B, C, D):
    """
    상태 1에서 상태 2로의 엔탈피 및 엔트로피 변화 계산 (파이썬 변환)
    """
    # 초기 및 최종 상태에서의 편차 함수 계산 (DEPFUN_VR 함수 필요)
    DH1, DS1 = DEPFUN_VR(P1, T1, Pc, Tc, w)
    DH2, DS2 = DEPFUN_VR(P2, T2, Pc, Tc, w)

    # 이상기체의 상태 변화 계산 (INTCP 함수 필요)
    delH_ig, delS_ig = INTCP(T1, T2, P1, P2, A, B, C, D)

    # 1->2 상태 변화량 계산
    DH = DH2 + delH_ig - DH1
    DS = DS2 + delS_ig - DS1

    return DH, DS