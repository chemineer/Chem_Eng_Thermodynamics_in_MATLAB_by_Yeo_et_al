import numpy as np
from Efun import Efun

def solve_temperature(P, Ti):
    """
    주어진 압력(P)과 초기 온도(Ti)에 대해 Efun(T, P) = 0이 되는 
    온도 T를 이분법(Bisection method)으로 구하는 함수
    """
    eps = 1.0e-5
    delT = 10.0

    # 온도구간 (T1, T2)의 초기화
    T1 = Ti
    f1 = Efun(T1, P)
    while f1 < 0:
        T1 -= delT
        f1 = Efun(T1, P)

    T2 = Ti + delT
    f2 = Efun(T2, P)
    while f2 > 0:
        T2 += delT
        f2 = Efun(T2, P)

    # 이분법(Bisection method)을 이용한 반복계산
    T = (T1 + T2) / 2.0
    while abs(T2 - T1) > eps:
        f1 = Efun(T1, P)
        T = (T1 + T2) / 2.0
        f = Efun(T, P)
        
        if f1 * f < 0:
            T2 = T
        else:
            T1 = T
            
    return T

# 메인 실행부
if __name__ == "__main__":
    # 케이스 1: P=100, Ti=600
    T_case1 = solve_temperature(100.0, 600.0)
    print(f'\n[Case 1: P=100.0 bar, Ti=600.0 K]')
    print(f'계산된 온도={T_case1:8.3f} K \n')

    # 케이스 2: P=200, Ti=700
    T_case2 = solve_temperature(200.0, 700.0)
    print(f'[Case 2: P=200.0 bar, Ti=700.0 K]')
    print(f'계산된 온도={T_case2:8.3f} K \n')