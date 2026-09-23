from __future__ import print_function, division
from scipy import integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as patches

rc('text', usetex=True)
# #rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

fig = plt.figure(figsize=(3,2.2))
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

ax.annotate('$x$', xy=(1.6, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='data', textcoords='offset points')
ax.annotate('$y$', xy=(0, 1.28), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='data', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#!python
# Definition of parameters
a = 2./3
b = 4./3
c = 1
d = 1

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([X[0]*(1-X[0]),
                    np.sin(X[1]/2)**2])


t_min = 0
t_max = 100
t = np.linspace(t_min, t_max, num=1000)
# initials conditions: 1 greenfly and 1 ladybird


initial_conditions = [np.array([1.1,np.pi/16]), 
                      np.array([0.9,np.pi/64]),
                      np.array([1.1,-np.pi/16]),
                      np.array([1.05,np.pi/32]),
                      np.array([0.92,-np.pi/32]),]
for X0 in initial_conditions:
    X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
    r, theta = X.T
    ax.plot(r*np.cos(theta), r*np.sin(theta),zorder=-3)

# ax.set_xlim([-1.2, 1.5])
# ax.set_ylim([-1.2, 1.5])

ir = np.array(initial_conditions)[:,0]
itheta = np.array(initial_conditions)[:,1]
ix = ir*np.cos(itheta)
iy = ir*np.sin(itheta)
ax.scatter(x=ix,y=iy,s=5,c=['C'+str(i) for i in range(9)][:len(ix)])

ax.axis('equal')

ax.set_ylim([-1.1, 1.3])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

# plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

style = "Simple, tail_width=0.5, head_width=4, head_length=8"
a3 = patches.FancyArrowPatch((0.8,0.2), (0.2, 0.8),
                             connectionstyle="arc3,rad=.36", arrowstyle=style, color='k')

plt.gca().add_patch(a3)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
