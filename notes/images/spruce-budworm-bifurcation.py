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
t_max = 1
t = np.linspace(t_min, t_max, num=1000)
# A = 1
# a = 2
# K = 1
R = 1
k = 10
K = k 
a = R
#x = A*np.exp(a*t)

solutions1 = []
solutions2 = []
solutions3 = []
for R in t:
    x_0 = np.roots([-R/k,R,(-1-R/k),R])
    if len(x_0) == 1:
        if not np.iscomplex(x_0[0]):
            solutions1.append(x_0[0])
            solutions2.append(x_0[0])
            solutions3.append(x_0[0])
        else:
            solutions1.append(None)
            solutions2.append(None)
            solutions3.append(None)
    else:
        if not np.iscomplex(x_0[0]):
            solutions1.append(x_0[0])
        else:
            solutions1.append(None)
        if not np.iscomplex(x_0[1]):
            solutions2.append(x_0[1])
        else:
            solutions2.append(None)
        if not np.iscomplex(x_0[2]):
            solutions3.append(x_0[2])
        else:
            solutions3.append(None)

# x1 = 0.5*(K+(K**2-4*t*K/a)**0.5)
# x2 = 0.5*(K-(K**2-4*t*K/a)**0.5)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0])
ax.set_xticklabels([0])
ax.set_yticks([0,k])#0,A/(1+(A/K)),K])
ax.set_yticklabels([0,"$k$"])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$R$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$x_0$', xy=(0.00, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# ax.plot(t, solutions1, '--', color='C4')
ax.plot(t, solutions1, color='C4')
ax.plot(t, solutions2, '--', color='C4')
ax.plot(t, solutions3, color='C4')
ax.plot(t, [0 for s in t], '--', color='C4', clip_on=False)
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

#ax.arrow( , 0, -1, head_length=0.1, head_width=0.05, arrowprops=dict(arrowstyle="->"))
# ax.annotate("$H$", xy=(0.75*K,0.5), xytext=(0.75*K, -0.7),
#             arrowprops=dict(arrowstyle="<-",lw=0.7), ha='center')

ax.annotate("", xy=(0.56, 0.2*k), xytext=(0.56, 0.74*k), arrowprops=dict(arrowstyle="<-", lw=0.7, color='C3'), ha='center')
ax.annotate("", xy=(0.38, 0.07*k), xytext=(0.38, 0.34*k), arrowprops=dict(arrowstyle="->", lw=0.7, color='C3'), ha='center')

ax.set_xlim([t_min, t_max])
ax.set_ylim([0, 1.2*K])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
