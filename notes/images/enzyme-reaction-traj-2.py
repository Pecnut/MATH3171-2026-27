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

fig = plt.figure(figsize=(2.2,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)
#ax.axis('equal')

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.annotate('$u$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$v$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# Definition of parameters
a = 0.19
b = 0.55

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([a - X[0] + X[0]**2*X[1],
                     b - X[0]**2*X[1] ])


t_min = 0
t_max = 100
t = np.linspace(t_min, t_max, num=1000)
# initials conditions: 1 greenfly and 1 ladybird
for i,X0 in enumerate([[0.1,0.1],
                        # [2,0.1],[3,2],
                        #[4,2]]
                        ]):
# for i,X0 in enumerate([[0.1,0.1],[0.1,0.4],[0.1,0.7],
#                        [0.2,1.5],[0.5,1.5],[1,1.5],
#                        [1.5,1],[1.5,0.5],[0.5,0.1]]):
    X0 = np.array(X0)
    X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
    greenflies, ladybirds = X.T
    plt.plot(greenflies,ladybirds,color='C2')

    if 1==1:#i <= 1:
        # Arrows
        # sample at 0, 1/3rd, and 2/3rd of curve
        adx0 = 30
        #adx1 = len(t) // 3
        #adx2 = adx1 * 2
        x = greenflies
        y = ladybirds
        arrow0 = x[adx0], y[adx0], x[adx0+1]-x[adx0], y[adx0+1]-y[adx0]
        #arrow1 = x[adx1+1], y[adx1+1], x[adx1]-x[adx1+1], y[adx1]-y[adx1+1]
        #arrow2 = x[adx2+1], y[adx2+1], x[adx2]-x[adx2+1], y[adx2]-y[adx2+1]
        # plt.arrow(*arrow0, shape='full', lw=0, length_includes_head=True,
        #           head_width=0.1,zorder=3,color='C2')

        prop = dict(arrowstyle="-|>,head_width=0.3,head_length=0.6",
                    shrinkA=0,shrinkB=0,fc='C2',ec='C2')

        plt.annotate("", xy=(x[adx0+1],y[adx0+1]), xytext=(x[adx0],y[adx0]), arrowprops=prop)


        #plt.arrow(*arrow1, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)
        #plt.arrow(*arrow2, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)

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

ax.set_ylim([0, 2.4])
# ax.set_xlim([0, 1.6])

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eqa
# ax.scatter([0],[1],color='k',zorder=5, clip_on=False)
# ax.scatter([0],[0],color='w',ec='k',zorder=5, clip_on=False)
ax.scatter([a+b],[b/(a+b)**2],color='k',ec='k',zorder=5, clip_on=False)

# Nullclines
u = np.linspace(0.1,2.1,100)
v = (u-a)/u**2
ax.plot(u,v,'--',color='C0',lw=0.7,zorder=4, clip_on=True)

u = np.linspace(0.1,2.1,100)
v = b/u**2
ax.plot(u,v,'--',color='C1',lw=0.7,zorder=4, clip_on=True)
#
# ax.set_xticks([0,1,1/g2])
# ax.set_xticklabels([0,1,'$1/\gamma_2$'])
# ax.set_yticks([0,1,1/g1])
# ax.set_yticklabels([0,1,'$1/\gamma_1$'])
#
# ax.text(1,1,'$\dot{x}<0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(0.2,0.2,'$\dot{x}>0$\n$\dot{y} > 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(0.15,1.1,'$\dot{x}>0$\n$\dot{y} < 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)
# ax.text(1.1,0.15,'$\dot{x}<0$\n$\dot{y} > 0$',ha='center',va='center',bbox=dict(fc='w',lw=0,alpha=0.7),fontsize=8)

#plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# t1 = ['$\gamma_1<1$','$\gamma_1>1$'][g1>1]
# t2 = ['$\gamma_2<1$','$\gamma_2>1$'][g2>1]
# tt = t1 + ", " + t2

# ax.set_title(tt,fontsize=12)
# plt.title('$\gamma_1>1$, $\gamma_2<1$')

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
# plt.savefig('lotka-volterra-3-phaseTEMP.pgf', transparent=True)


plt.show()
