import numpy as np

def Z_PR(Tc=126.1, Pc=33.94, w=0.04, T=100.0, P=4.119):
    """
    Peng-Robinson 3차 방정식의 근(Z) 계산 (파이썬 변환)
    """
    R = 8.3143  # J/mol-K
    Tr = T / Tc  # 환산 온도
    
    # 방정식 파라미터 계산
    k = 0.37464 + 1.54226 * w - 0.26993 * w**2.0
    alpha = (1.0 + k * (1.0 - Tr**0.5))**2.0
    ac = 0.45723553 * (R**2 * Tc**2.0) / Pc
    a = ac * alpha
    b = 0.07779607 * R * Tc / Pc

    A = (a * P) / (R**2 * T**2.0)
    B = (b * P) / (R * T)

    # 3차 방정식 계수
    a3 = 1.0
    a2 = -(1.0 - B)
    a1 = (A - 3.0 * B**2 - 2.0 * B)
    a0 = -(A * B - B**2 - B**3)

    # 3차 방정식의 풀이
    p = [a3, a2, a1, a0]
    Z = np.roots(p)

    # 결과 출력
    print("\nPeng-Robinson 3차방정식의 근 :")
    for val in Z:
        print(f"{val:10.5f}")
        
    return Z

# 함수 실행 예시
if __name__ == "__main__":
    Z_PR()