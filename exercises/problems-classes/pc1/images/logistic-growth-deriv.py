from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

t_min = 0
t_max = 1.4
t = np.linspace(t_min, t_max, num=1000)
A = 1
a = 2
K = 1
#x = A*np.exp(a*t)
x = a * t * (1 - t / K)

fig = plt.figure(figsize=(3, 2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0, K])
ax.set_xticklabels([0, "$N$"])
ax.set_yticks([0])  # 0,A/(1+(A/K)),K])
ax.set_yticklabels([0])  # (["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
# ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$x$', xy=(1, 0.68), xytext=(0, -2 * ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$\displaystyle\\frac{\mathrm{d}I}{\mathrm{d}t}$', xy=(0.00, 1), xytext=(-2 * ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x, color='C2')

ax.scatter([K], [0], color='C2', zorder=3, clip_on=False)
ax.scatter([0], [0], color='w', ec='C2', zorder=3, clip_on=False)

ax.annotate("", xy=(0.6, 0), xytext=(0.4, 0),
            arrowprops=dict(arrowstyle="->",lw=0.6,ec='C2'),zorder=-3)
ax.annotate("", xy=(1.2, 0), xytext=(1.4, 0),
            arrowprops=dict(arrowstyle="->",lw=0.6,ec='C2'),zorder=-3)

ax.set_xlim([t_min, t_max])
#ax.set_ylim([0, 1])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
