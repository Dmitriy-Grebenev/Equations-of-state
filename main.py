from math import exp
from constants import *

"""

"""
def LeeKessler(T = 273, T_k = 647.3, P = 101325, P_k = 22.1 * 10**6, V_zero = 1, omega = 0.644):

    T_r = T / T_k
    P_r = P / P_k
    V_r_zero = (P_k * V_zero) / (R * T_k)
    
    # Расчёт для простого вещества.
    B = b1[0] - b2[0] / T_r - b3[0] / (T_r * T_r) - b4[0] / (T_r ** 3)
    C = c1[0] - c2[0] / T_r + c3[0] / (T_r ** 3)
    D = d1_10_4[0] + d2_10_4[0] / T_r

    Z_zero  =   (1 + B / V_r_zero 
                + C / (V_r_zero ** 2) 
                + D / (V_r_zero ** 5) 
                + c4[0] / (T_r ** 3 * V_r_zero ** 2) 
                * (beta[0] + gamma[0] / (V_r_zero ** 2))
                * exp(-gamma[0]/(V_r_zero ** 2)))

    # Расчёт для эталонного вещества.
    B = b1[1] - b2[1] / T_r - b3[1] / (T_r * T_r) - b4[1] / (T_r ** 3)
    C = c1[1] - c2[1] / T_r + c3[1] / (T_r ** 3)
    D = d1_10_4[1] + d2_10_4[1] / T_r

    Z_R  =   (1 + B / V_r_zero 
                + C / (V_r_zero ** 2) 
                + D / (V_r_zero ** 5) 
                + c4[1] / (T_r ** 3 * V_r_zero ** 2) 
                * (beta[1] + gamma[1] / (V_r_zero ** 2))
                * exp(-gamma[1]/(V_r_zero ** 2)))
    
    Z = Z_zero + omega / omega_R * (Z_R - Z_zero)
    return Z


print(LeeKessler())