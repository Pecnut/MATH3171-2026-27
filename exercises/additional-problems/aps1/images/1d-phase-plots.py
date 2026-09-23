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
t_max = 20
t = np.linspace(t_min, t_max, num=1000)
# A = 0.5
# a = 2
K = 1
#x = A*np.exp(a*t)
# x = a*t*(1-t/K)*(t/A-1)
# x = t*(t-1)
x = t/(t+K)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0])
# ax.set_xticklabels([0,"$A$","$K$"])
ax.set_yticks([0,1])#0,A/(1+(A/K)),K])
ax.set_yticklabels([0,"$r$"])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$\displaystyle\\frac{\mathrm{d}x}{\mathrm{d}t}$', xy=(0.00, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

arrowprops = dict(arrowstyle="->, head_length = 0.4, head_width = .3", shrinkA = 0, shrinkB = 0, color='C3', patchA = None, patchB = None, relpos = (0,0))
ax.annotate("", xy=(5, 0), xytext=(4.9*K, 0), arrowprops=arrowprops)
# ax.annotate("", xy=(0.800*K, 0), xytext=(0.79*K, 0), arrowprops=arrowprops)
# ax.annotate("", xy=(1.150*K, 0), xytext=(1.14*K, 0), arrowprops=arrowprops)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.axhline(1,dashes=(5,5),lw=0.7,c='k')

ax.plot(t, x, color='C2')
# ax.scatter([K],[0],color='C2',zorder=3, clip_on=False)
ax.scatter([0],[0],color='C2',zorder=3, clip_on=False)
# ax.scatter([1],[0],color='w',ec='C2',zorder=3, clip_on=False)

# ax.plot(t, x-0.25, color='C2', alpha=1)
# d = 0.142
# ax.scatter([K-d],[0],color='C2',zorder=3, clip_on=False, alpha=1)
# ax.scatter([0+d],[0],color='w',ec='C2',zorder=3, clip_on=False, alpha=1)
#
# ax.plot(t, x-0.5, color='C2', alpha=1)
# d = 0.5
# from matplotlib.markers import MarkerStyle
# ax.scatter([0+d],[0],color='C2',ec='C2',zorder=3, clip_on=False, alpha=1,
#            marker=MarkerStyle("o", fillstyle="right"))
# ax.scatter([0+d],[0],color='w',ec='C2',zorder=3, clip_on=False, alpha=1,
#            marker=MarkerStyle("o", fillstyle="left"))
#
#
# ax.plot(t, x-0.75, color='C2', alpha=1)

#ax.arrow( , 0, -1, head_length=0.1, head_width=0.05, arrowprops=dict(arrowstyle="->"))
#ax.annotate("$H$", xy=(0.75*K,0.5), xytext=(0.75*K, -0.7),
#            arrowprops=dict(arrowstyle="<-",lw=0.7), ha='center')


ax.set_xlim([t_min, t_max])
ax.set_ylim([0, 1.4])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
