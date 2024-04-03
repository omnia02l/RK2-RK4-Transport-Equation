//Omnia Lahdhiri
import numpy as np
import matplotlib.pyplot as plt
c = 1.0
h = 0.1
tau = 0.1
T = 2.0
N = 2.0
x_valeurs = np.arange(0, N, h)
t_valeurs = np.arange(0, T, tau)
def u0(x) :
    return np.sin(x)
def phi(t):
 return 2*t-1
def source(x, t):
 return np.exp(t**2)+x
udiff = np.zeros(len(x_valeurs))
