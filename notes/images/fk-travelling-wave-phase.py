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

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.set_xticks([0,1])
ax.set_xticklabels([0,1])
ax.set_yticks([0])
ax.set_yticklabels([0])

ax.annotate('$u$', xy=(1, 0.535), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$v$', xy=(0.15, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


#!python
# Definition of parameters
c = 1

def dX_dt(X, t=0):
    """ Return the growth rate of greenfly and ladybird populations. """
    return np.array([X[1] ,
                    -c*X[1] - X[0]*(1-X[0]) ])


t_min = 0
t_max = 50
t = np.linspace(t_min, t_max, num=1000)
# initials conditions: 1 greenfly and 1 ladybird
X0 = np.array([1-1e-4,0])
X = integrate.odeint(dX_dt, X0, t)                # >>> 'Integration successful.'
greenflies, ladybirds = X.T
ax.plot(greenflies, ladybirds, label='greenflies, $x(t)$\hspace{-14pt}', zorder=3, clip_on=False,color='C2')
# ax.plot(t, ladybirds, '--', label='ladybirds, $y(t)$\hspace{-14pt}', zorder=-3)

adx0 = 300
# adx0 = 450
x = greenflies
y = ladybirds
arrow0 = x[adx0], y[adx0], x[adx0+1]-x[adx0], y[adx0+1]-y[adx0]
prop = dict(arrowstyle="-|>,head_width=0.3,head_length=0.6",
            shrinkA=0,shrinkB=0,fc='C2',ec='C2')

plt.annotate("", xy=(x[adx0+1],y[adx0+1]), xytext=(x[adx0],y[adx0]), arrowprops=prop)


# from matplotlib.markers import MarkerStyle
ax.scatter([0],[0],color='C2',ec='C2',zorder=4, clip_on=False, alpha=1)
ax.scatter([1],[0],color='w',ec='C2',zorder=4, clip_on=False, alpha=1)

# Add nullclines
u = np.linspace(-0.2,1.2,100)
u_nullcline = 0*u
v_nullcline = -u*(1-u)/c
ax.plot(u, u_nullcline, 'C0', linestyle='dashed', zorder=1, alpha=0.5)
ax.plot(u, v_nullcline, 'C1', linestyle='dashed', zorder=1, alpha=0.5)

# ax.set_xlim([0,1.1])
ax.set_xlim([-0.2,1.1])
ax.set_ylim([-0.27, 0.25])

plt.title(f'$c={c}$',fontsize=12)


plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)


# plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
