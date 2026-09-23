from __future__ import print_function, division
from scipy import integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

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

ax.set_xticks([0])
ax.set_xticklabels([0])
ax.set_yticks([0,1])
ax.set_yticklabels([0,1])

ax.annotate('$z$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$u,v$', xy=(0.5, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#!python
# Definition of parameters
c = 2

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([X[1] ,
                    -c*X[1] - 0.5*X[0]*(1-X[0]) ])


t_min = -25
t_max = 25
t = np.linspace(t_min, t_max, num=1000)
# initials conditions: 1 greenfly and 1 ladybird
X0 = np.array([1-1e-2,0])
X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
greenflies, ladybirds = X.T
ax.plot(t, 1-greenflies, label='$u$', zorder=4, clip_on=False, color='C3')
ax.plot(t, greenflies, label='$v$', zorder=4, clip_on=False,color='C7')
# ax.plot(t, ladybirds, '--', label='ladybirds, $y(t)$\hspace{-14pt}', zorder=-3)

ax.set_xlim([t_min, t_max*1.01])
ax.set_ylim([0, 1.2])
ax.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.title('$c=1$',fontsize=12)


plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)


# plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
