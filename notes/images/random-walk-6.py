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

fig = plt.figure(figsize=(3,3))
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

ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$t$', xy=(0, 110), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
             xycoords='data', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#!python
# Definition of parameters
p = 0.9

t_min = 0
t_max = 100
t = np.arange(t_min,t_max)

max_x = 0
final_x = []
for j in range(200):
    walk = np.zeros(t_max-t_min)
    for i in t[1:]:
        if np.random.rand() < p:
            walk[i] = walk[i-1] + 1
        else:
            walk[i] = walk[i-1] - 1

    ax.plot(walk, t, zorder=-3,color='C0',alpha=0.2)

    max_x = max(max(abs(walk)),max_x)
    final_x.append(walk[-1])

ax.set_ylim([t_min, t_max*1.1])
ax.axvline(sum(final_x)/len(final_x),dashes=(2,2),color='k',linewidth=0.8, ymax=0.93)
#ax.set_xlim([-max_x*1.05, max_x*1.05])
ax.set_aspect('equal')



plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
