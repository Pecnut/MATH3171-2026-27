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
t_max = 11
t = np.linspace(t_min, t_max, num=1000)
R = 0.45
k = 10.0
x = np.linspace(0,10,1000)
h = R*(1 - t/k)
g = x/(1 + t**2);

a = 0.67
b = 2.05
c = 7.29

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0,a,b,c,k])
ax.set_xticklabels([0,"$a$","$b$","$c$","$k$"])
ax.set_yticks([0,R])#0,A/(1+(A/K)),K])
ax.set_yticklabels([0,"$R$"])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])

ax.vlines(a,color='k',linestyles='dashed',linewidth=0.8,ymin=0,ymax=R*(1 - a/k))
ax.vlines(b,color='k',linestyles='dashed',linewidth=0.8,ymin=0,ymax=R*(1 - b/k))
ax.vlines(c,color='k',linestyles='dashed',linewidth=0.8,ymin=0,ymax=R*(1 - c/k))

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$x$', xy=(1, 0.0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
# ax.annotate('$g,h$', xy=(0.00, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, g, color='C0', label='$g$')
ax.plot(t, h, '--', color='C1', label='$h$')
# ax.scatter([K],[0],color='C2',zorder=3, clip_on=False)
# ax.scatter([0],[0],color='C2',zorder=3, clip_on=False)
# ax.scatter([A],[0],color='w',ec='C2',zorder=3, clip_on=False)

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
ax.set_ylim([0, None])
plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
