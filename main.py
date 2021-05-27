from gramm_integrate import make_matrix as integ
from gramm_scalar import make_matrix as scal
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt


f1 = np.sin
a, b = 0, np.pi
n = 10
G1, d1 = integ(f1, n, a, b)
c1 = solve(G1, d1)
xi = np.linspace(a, b, num=n)
G2, d2 = scal(xi, f1(xi))
c2 = solve(G2, d2)

def f2(x, c):
    return sum([c[i] * x ** i for i in range(n)])
x = np.linspace(a, 2 * b, num=100)
ytrue  = f1(x)
ynew1 = f2(x, c1)
ynew2 = f2(x, c2)
plt.plot(x, ynew1, color='red')
plt.plot(x, ynew2, color='green')
plt.plot(x, ytrue, color='blue')
plt.show()