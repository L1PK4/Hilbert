import numpy as np
from itertools import starmap

def make_matrix(x, y):
    n = len(x)
    g = np.array([[ sum(list(map(lambda xk : xk ** (i + j), x))) for i in range(n)] for j in range(n)])
    d = np.array([sum(list(starmap(lambda xk, yk : yk * (xk ** i), zip(x,y) ))) for i in range(n)])
    return g, d