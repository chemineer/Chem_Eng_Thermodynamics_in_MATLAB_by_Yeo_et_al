import numpy as np
from DEPFUN_PR import DEPFUN_PR
from INTCP import INTCP

def DELHS_PR(T1, T2, P1, P2, Pc, Tc, w, A, B, C, D):
    """
    상태 1에서 상태 2로의 엔탈피 및 엔트로피 변화 계산 (파이썬 변환)
    """
    # 초기 및 최종 상태에서의 편차 함수 계산 (DEPFUN_PR 함수 필요)
    Z1, V1, DH1, DS1, DU1, DG1, DA1, Sc1, Ac1 = DEPFUN_PR(P1, T1, Pc, Tc, w)
    Z2, V2, DH2, DS2, DU2, DG2, DA2, Sc2, Ac2 = DEPFUN_PR(P2, T2, Pc, Tc, w)

    # 이상기체의 상태 변화 계산 (INTCP 함수 필요)
    delH_ig, delS_ig = INTCP(T1, T2, P1, P2, A, B, C, D)

    # MATLAB의 length() 확인을 위해 Z값이 배열인지 단일 값인지 확인
    Z1_arr = np.atleast_1d(Z1)
    Z2_arr = np.atleast_1d(Z2)

    # 1->2 상태 변화량 계산 (배열 크기에 따른 분기 처리)
    if len(Z1_arr) == 1 and len(Z2_arr) == 1:
        DH = DH2 + delH_ig - DH1
        DS = DS2 + delS_ig - DS1
    elif len(Z1_arr) == 1 and len(Z2_arr) > 1:
        DH = DH2 + delH_ig - DH1
        DS = DS2 + delS_ig - DS1
    elif len(Z1_arr) > 1 and len(Z2_arr) == 1:
        DH = DH2 + delH_ig - DH1
        DS = DS2 + delS_ig - DS1
    else:
        DH = DH2 + delH_ig - DH1
        DS = DS2 + delS_ig - DS1

    return Z1, Z2, DH, DS