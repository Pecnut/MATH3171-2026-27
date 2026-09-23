from __future__ import print_function, division
from scipy.integrate import odeint
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(3, 2.2))
ax = fig.subplots(1, 1)

# Definition of parameters
nu = 0.2
m = 1
g = 10
l = 5

b = nu/m
c = g/l

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

y0 = [np.pi/2, 0.0]

t_min = 0
t_max = 50
t = np.linspace(t_min, t_max, num=1000)

X = odeint(pend, y0, t, args=(b, c))

theta, omega = X.T
ax.plot(t, theta)

ax.set_yticks([np.pi/4*i for i in [-2,-1,0,1,2]])
ax.set_yticklabels(["$-\pi/2$", "$-\pi/4$", 0, "$\pi/4$", "$\pi/2$"])

plt.show()
