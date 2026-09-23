from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

t_min = -1
t_max = 1
t = np.linspace(t_min, t_max, num=1000)
# A = 1
# a = 2
# K = 1
#x = A*np.exp(a*t)
x1 = (t)**0.5
x2 = -(t)**0.5
x3 = 0
x4 = 0

fig = plt.figure(figsize=(1.8,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([])
ax.set_xticklabels([])
ax.set_yticks([])#0,A/(1+(A/K)),K])
ax.set_yticklabels([])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$p$', xy=(1, 0.5), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$x_0$', xy=(0.5, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x1, color='C4',zorder=3,clip_on=False)
ax.plot(t, x2, color='C4',zorder=3,clip_on=False)
ax.plot([-1,0], [0,0], color='C4',zorder=3,clip_on=False)
ax.plot([0, 1], [0, 0], '--', color='C4',zorder=3,clip_on=False)
# ax.scatter([a*K/4],[K/2],color='C4',zorder=3, clip_on=False,marker='*')
# ax.scatter([K],[0],color='C2',zorder=3, clip_on=False)
# ax.scatter([0],[0],color='w',ec='C2',zorder=3, clip_on=False)

# ax.plot(t, x-0.25, color='C2', alpha=1)
# d = 0.142
# ax.scatter([K-d],[0],color='C2',zorder=3, clip_on=False, alpha=1)
# ax.scatter([0+d],[0],color='w',ec='C2',zorder=3, clip_on=False, alpha=1)

# ax.plot(t, x-0.5, color='C2', alpha=1)
# d = 0.5
# from matplotlib.markers import MarkerStyle
# ax.scatter([0+d],[0],color='C2',ec='C2',zorder=3, clip_on=False, alpha=1,
#            marker=MarkerStyle("o", fillstyle="right"))
# ax.scatter([0+d],[0],color='w',ec='C2',zorder=3, clip_on=False, alpha=1,
#            marker=MarkerStyle("o", fillstyle="left"))


# ax.plot(t, x-0.75, color='C2', alpha=1)

ax.spines['bottom'].set_color('#aaaaaa')
ax.spines['left'].set_color('#aaaaaa')
ax.text(0.6,0.6,"$x_0=\sqrt{p}$",rotation=40,fontsize=9,color='C4',ha='center',va='center')
ax.text(0.6,-0.6,"$x_0=-\sqrt{p}$",rotation=-40,fontsize=9,color='C4',ha='center',va='center')
ax.text(-0.5,0.1,"$x_0=0$",rotation=0,fontsize=9,color='C4',ha='center',va='center')

#ax.arrow( , 0, -1, head_length=0.1, head_width=0.05, arrowprops=dict(arrowstyle="->"))
# ax.annotate("$x_0=\sqrt{p}$", xy=(0.3,0.5), xytext=(0.55, 0.1), fontsize=10,
#             arrowprops=dict(arrowstyle="->",lw=0.7,color='C4'), ha='center', va='bottom', color='C4')
# ax.annotate("$x_0=-\sqrt{p}$", xy=(0.3, -0.5), xytext=(0.55, -0.1), fontsize=10,
#             arrowprops=dict(arrowstyle="->",lw=0.7,color='C4'), ha='center', va='top', color='C4')
# ax.annotate("$x_0=0$", xy=(-0.5, 0.05), xytext=(-0.5, 0.45), fontsize=10,
#             arrowprops=dict(arrowstyle="->",lw=0.7,color='C4'), ha='center', va='bottom', color='C4')
# ax.annotate("", xy=(0.2, 0.05), xytext=(-0.5, 0.43), fontsize=10,
#             arrowprops=dict(arrowstyle="->",lw=0.7,color='C4'), ha='center', va='bottom', color='C4')


ax.set_xlim([t_min, t_max])
# ax.set_ylim([0, 1.2*K])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.savefig('bifurcation-pitchfork.pgf')
plt.show()
