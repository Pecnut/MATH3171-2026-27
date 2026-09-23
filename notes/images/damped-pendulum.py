from __future__ import print_function, division
from scipy.integrate import odeint
from scipy import integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
# #rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

fig = plt.figure(figsize=(3, 2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

# ax.set_xticks([0])
# ax.set_xticklabels([0])
# ax.set_yticks([0,1])
# ax.set_yticklabels([0,1])

ax.annotate('$t$', xy=(1, 0.44), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$\\theta$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
             xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#!python
# Definition of parameters
#nu = 0.2
nu = 10
m = 1
g = 10
l = 5

b = nu/m
c = g/l


def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

#b = 0.25
#c = 5.0

y0 = [np.pi/2, 0.0]

t_min = 0
t_max = 50
t = np.linspace(t_min, t_max, num=1000)

X = odeint(pend, y0, t, args=(b, c))

theta, omega = X.T
ax.plot(t, theta, label='$\\theta$', zorder=-3)

ax.set_xlim([t_min, t_max*1.01])
ax.set_ylim([-np.pi/2, np.pi/2*1.3])

ax.set_yticks([np.pi/4*i for i in [-2,-1,0,1,2]])
ax.set_yticklabels(["$-\pi/2$", "$-\pi/4$", 0, "$\pi/4$", "$\pi/2$"])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

# leg = plt.legend(ncol=1, frameon=True, framealpha=0.8,
#                  borderpad=0, borderaxespad=0)
# leg.get_frame().set_linewidth(0.0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
