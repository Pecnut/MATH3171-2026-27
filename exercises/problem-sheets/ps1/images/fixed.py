from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

A = 1
a = 13
K = 0.5
t_min = 0
t_max = 1.1*K
alpha = 0.002
t = np.linspace(t_min, t_max, num=1000)

#x = A*np.exp(a*t)
# x = np.exp(-t**2/0.001)
x = a*t*(1-t/K)-(1-np.exp(-t**2/alpha))

fig = plt.figure(figsize=(2.5,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0,K/2,K,alpha**0.5])
ax.set_xticklabels([0,"$q/2$","$q$","$\sqrt{\\alpha}$"])
ax.set_yticks([-1,0,a*K/4-1])#0,A/(1+(A/K)),K])
ax.set_yticklabels(["$-1$",0,"$rq/4-1$"])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$\widehat{x}$', xy=(1, 0.52), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$\displaystyle\\frac{\mathrm{d}\widehat{x}}{\mathrm{d}\widehat{t}}$', xy=(0.00, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

# arrowprops = dict(arrowstyle="->, head_length = 0.4, head_width = .3", shrinkA = 0, shrinkB = 0, color='C3', patchA = None, patchB = None, relpos = (0,0))
# ax.annotate("", xy=(0.500*K, 0), xytext=(0.49*K, 0), arrowprops=arrowprops)
# ax.annotate("", xy=(0.900*K, 0), xytext=(0.91*K, 0), arrowprops=arrowprops)
# ax.annotate("", xy=(0.100*K, 0), xytext=(0.11*K, 0), arrowprops=arrowprops)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x, color='C2')
# ax.plot(t, y, color='C4')

# ax.scatter([K],[0],color='C2',zorder=3, clip_on=False, alpha=1)
# ax.scatter([0],[0],color='w',ec='C2',zorder=3, clip_on=False, alpha=1)

ax.set_xlim([t_min, t_max])
ax.set_ylim([-1, 1.6])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
