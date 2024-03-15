 //Omnia_Lahdhiri
 import numpy as np
 import matplotlib.pyplot as plt
 c = 1.0
 h = 0.1
 tau = 0.01
 T = 2.0
 N = 2.0
 x_valeurs = np.arange(0, N, h)
 t_valeurs = np.arange(0, T, tau)
 def u0(x):
 return np.cos(2*x)
 def phi(t):
 return np.exp(t**2)
 def source(x, t):
 return np.sin(2*x*t)
 udiff = np.zeros(len(x_valeurs))
 urk2 = np.zeros(len(x_valeurs))
 urk4 = np.zeros(len(x_valeurs))
 for i in range(len(x_valeurs)):
 if x_valeurs[i] < c * t_valeurs[0]:
        udiff[i] = u0(x_valeurs[i])
        urk2[i] = u0(x_valeurs[i])
        urk4[i] = u0(x_valeurs[i])
 else:
        udiff[i] = phi(t_valeurs[0])
        urk2[i] = phi(t_valeurs[0])
        urk4[i] = phi(t_valeurs[0])
 for i in range(1, len(x_valeurs)):
    udiff[i] = udiff[i] - c * (tau / h) * (udiff[i] - udiff[i-1]) + tau * source(x_valeurs[i] , 0.75)
 for i in range(len(x_valeurs)):
    k1_t_rk2 = tau * (source(x_valeurs[i] , 0.75) - c * (urk2[i] - urk2[i-1]) / (2 * h))
    k1_x_rk2 = c * tau * (urk2[i])
 k2_t_rk2 = tau * (source(x_valeurs[i] , 0.75 + (tau/2)) - c * (urk2[i] + k1_x_rk2 / 2 - urk2[i-1] - k1_t_rk2 / 2) / (2 *
 h))
    k2_x_rk2 = c * tau * (urk2[i] + k1_x_rk2 / 2)
  u_t_moitie_rk2 = (urk2[i] + urk2[i-1]) / 2 + k2_t_rk2
    u_x_nouv_rk2 = urk2[i] + (k1_x_rk2 + k2_x_rk2) / 2
    k1_rk2 = tau * (source(x_valeurs[i] , 0.75) - c * (u_x_nouv_rk2 - urk2[i-1]) / (2 * h))
    k2_rk2 = tau * (source(x_valeurs[i] , 0.75 + (tau/2)) - c * (u_x_nouv_rk2 - urk2[i-1] - k1_rk2 / 2) / (2 * h))
    urk2[i] = urk2[i] + (k1_rk2 + k2_rk2) / 2
 for i in range(len(x_valeurs)):
    k1_t_rk4 = tau * (source(x_valeurs[i] , 0.75) - c * (urk4[i] - urk4[i-1]) / (2 * h))
    k1_x_rk4 = c * tau * (urk4[i])
    k2_t_rk4 = tau * (source(x_valeurs[i] , 0.75 + (tau/2)) - c * (urk4[i] + k1_x_rk4 / 2 - urk4[i-1] - k1_t_rk4 / 2) / (2 *
 h))
   k2_x_rk4 = c * tau * (urk4[i] + k1_x_rk4 / 2)
   k3_t_rk4 = tau * (source(x_valeurs[i] , 0.75 + (tau/2)) - c * (urk4[i] + k2_x_rk4 / 2 - urk4[i-1] - k2_t_rk4 / 2) / (2 *
 h))
   k3_x_rk4 = c * tau * (urk4[i] + k2_x_rk4 / 2)
   k4_t_rk4 = tau * (source(x_valeurs[i] , 0.75 + tau) - c * (urk4[i] + k3_x_rk4 - urk4[i-1] - k3_t_rk4) / (2 * h))
   k4_x_rk4 = c * tau * (urk4[i] + k3_x_rk4)
   urk4[i] = urk4[i]
 diff_rk2 = np.abs(urk2 - udiff)
 diff_rk4 = np.abs(urk4 - udiff)
 //ceci est un commentaire