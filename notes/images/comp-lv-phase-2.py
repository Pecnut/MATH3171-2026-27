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
#ax.axis('equal')

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$y$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# Definition of parameters
g1 = 1/1.4
g2 = 1.4
b = 1

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([X[0]*(1-X[0]-g1*X[1]),
                     b*X[1]*(1-X[1]-g2*X[0]) ])


# t_min = 0
# t_max = 15
# t = np.linspace(t_min, t_max, num=1000)
# # initials conditions: 1 greenfly and 1 ladybird
# for i,y0 in enumerate([i*i for i in np.linspace(np.sqrt(0.2),np.sqrt(0.7),3)]):
#     X0 = np.array([1,y0])
#     X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
#     greenflies, ladybirds = X.T
#     plt.plot(greenflies,ladybirds,color='C2')
#
#     if i <= 1:
#         # Arrows
#         # sample at 0, 1/3rd, and 2/3rd of curve
#         adx0 = 130
#         #adx1 = len(t) // 3
#         #adx2 = adx1 * 2
#         x = greenflies
#         y = ladybirds
#         arrow0 = x[adx0], y[adx0], x[adx0+1]-x[adx0], y[adx0+1]-y[adx0]
#         #arrow1 = x[adx1+1], y[adx1+1], x[adx1]-x[adx1+1], y[adx1]-y[adx1+1]
#         #arrow2 = x[adx2+1], y[adx2+1], x[adx2]-x[adx2+1], y[adx2]-y[adx2+1]
#         plt.arrow(*arrow0, shape='full', lw=0, length_includes_head=True,
#                   head_width=0.2,zorder=3,color='C2')
#         #plt.arrow(*arrow1, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)
#         #plt.arrow(*arrow2, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)
#
# for X0 in [[0.01,0],[0,7]]:
#     X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
#     greenflies, ladybirds = X.T
#     plt.plot(greenflies,ladybirds,color='C4',zorder=3)
#     adx0 = 15
#     x = greenflies
#     y = ladybirds
# arrow0 = 0,2.5, 0,-0.1
# plt.arrow(*arrow0, shape='full', lw=0, length_includes_head=True,
#           head_width=0.2,zorder=3,color='C4', clip_on=False)
# arrow0 = 2.5,0, 0.1,0
# plt.arrow(*arrow0, shape='full', lw=0, length_includes_head=True,
#           head_width=0.2,zorder=3,color='C4', clip_on=False)

ax.set_ylim([0, 1.6])
ax.set_xlim([0, 1.6])

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eqa
# ax.scatter([0],[1],color='k',zorder=5, clip_on=False)
# ax.scatter([0],[0],color='w',ec='k',zorder=5, clip_on=False)
ax.scatter([0],[0],color='w',ec='k',zorder=5, clip_on=False)
ax.scatter([1],[0],color='w',ec='k',zorder=5, clip_on=False)
ax.scatter([0],[1],color='w',ec='k',zorder=5, clip_on=False)

# Nullclines
ax.plot([0,0],[0,1.6],'--',color='C0',lw=0.7,zorder=4, clip_on=False)
ax.plot([0,1.6],[0,0],'--',color='C1',lw=0.7,zorder=4, clip_on=False)
ax.plot([1,0],[0,1/g1],'--',color='C0',lw=0.7,zorder=1)
ax.plot([0,1/g2],[1,0],'--',color='C1',lw=0.7,zorder=1)

ax.set_xticks([0,1,1/g2])
ax.set_xticklabels([0,1,'$1/\gamma_2$'])
ax.set_yticks([0,1,1/g1])
ax.set_yticklabels([0,1,'$1/\gamma_1$'])

# ax.text(1,1,'$\dot{x}<0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(0.2,0.2,'$\dot{x}>0$\n$\dot{y} > 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(0.5,0.5,'$\dot{x}>0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(2,2,'$\dot{x}<0$\n$\dot{y} > 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7))
# ax.text(0.5,2,'$\dot{x}<0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7))
# ax.text(0.5,0.5,'$\dot{x}>0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7))

#plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
t1 = ['$\gamma_1<1$','$\gamma_1>1$'][g1>1]
t2 = ['$\gamma_2<1$','$\gamma_2>1$'][g2>1]
tt = t1 + ", " + t2

ax.set_title(tt,fontsize=12)
# plt.title('$\gamma_1>1$, $\gamma_2<1$')

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.savefig('lotka-volterra-3-phaseTEMP.pgf', transparent=True)


plt.show()
