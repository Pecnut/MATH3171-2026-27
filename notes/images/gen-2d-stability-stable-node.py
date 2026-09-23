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

# ax.set_xticks([0])
# ax.set_xticklabels([0])
# ax.set_yticks([0,1])
# ax.set_yticklabels([0,1])

ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$y$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# Definition of parameters
a = 1
b = 1
c = 0.1
d = 1

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([a*X[0] + b*X[1] ,
                     c*X[0] + d*X[1] ])

t_min = 0
t_max = 15
t = np.linspace(t_min, t_max, num=1000)
# initials conditions: 1 greenfly and 1 ladybird
start_points = [[0.01,0.01],[0.01,-0.01]]
for i,x0y0 in enumerate(start_points):
    X0 = np.array(x0y0)
    X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
    greenflies, ladybirds = X.T
    plt.plot(greenflies,ladybirds,color='C2')

    if i <= 1:
        # Arrows
        # sample at 0, 1/3rd, and 2/3rd of curve
        adx0 = 130
        #adx1 = len(t) // 3
        #adx2 = adx1 * 2
        x = greenflies
        y = ladybirds
        arrow0 = x[adx0], y[adx0], x[adx0+1]-x[adx0], y[adx0+1]-y[adx0]
        #arrow1 = x[adx1+1], y[adx1+1], x[adx1]-x[adx1+1], y[adx1]-y[adx1+1]
        #arrow2 = x[adx2+1], y[adx2+1], x[adx2]-x[adx2+1], y[adx2]-y[adx2+1]
        plt.arrow(*arrow0, shape='full', lw=0, length_includes_head=True,
                  head_width=0.2,zorder=3,color='C2')
        #plt.arrow(*arrow1, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)
        #plt.arrow(*arrow2, shape='full', lw=0, length_includes_head=True, head_width=0.12,zorder=3)

# for X0 in [[0.01,0],[0,7]]:
#     X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
#     greenflies, ladybirds = X.T
#     plt.plot(greenflies,ladybirds,color='C4',zorder=3)
#     adx0 = 15
#     x = greenflies
#     y = ladybirds


ax.set_ylim([-2.9, 2.9])
ax.set_xlim([-2.9, 2.9])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#ax.scatter([1],[1],color='C2',zorder=5, clip_on=False)
ax.scatter([0],[0],color='w',ec='C4',zorder=5, clip_on=False)

#plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))


# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
# plt.savefig('lotka-volterra-3-phaseTEMP.pgf', transparent=True)


plt.show()
