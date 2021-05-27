import scipy.integrate as integrate
import numpy as np

def make_matrix(func, n, a, b):
    G = np.array([[integrate.quad(lambda x : x ** (i + j), a, b)[0] for i in range(n)] for j in range(n)])
    d = np.array([integrate.quad(lambda x : func(x) * x ** j, a, b)[0] for j in range(n)])
    return G, d