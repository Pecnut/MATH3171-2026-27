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

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

# alpha = 0.9;
alpha = 0.2;
beta = 0.3;
c = np.sqrt(4*alpha*(1-beta))

ax.set_xticks([0])
ax.set_xticklabels([0])
ax.set_yticks([0,beta,1-beta,1])
ax.set_yticklabels([0,'$\\beta$','$1-\\beta$',1])

ax.annotate('$z$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
# ax.annotate('$u$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


N = 200
L = 200
dx = L/N



x = np.linspace(0, L, N, endpoint=False)
u0 = 0*x + 1;
u0[0:10] = beta

v0 = 0*x;
v0[0:10] = 1 - beta

D2 = np.eye(N, k = -1) - 2*np.eye(N) + np.eye(N,k = 1)
#D2[0][N-1] = 1;
#D2[N-1][0] = 1;
D2 = D2/dx**2
D2[0][0] = -1;
D2[0][1] = 1;
D2[N-1][N-1] = 1;
D2[N-1][N-2] = -1;

usol0 = np.concatenate((u0, v0))

def du_dt(usol, t):
    u = usol[0:N]
    v = usol[N:2*N]
    u1 = u*(1-u-v)
    v1 = alpha*v*(u-beta) + D2.dot(v)
    return np.concatenate((u1, v1))

Nt = 10000
ts = np.linspace(0, 100, Nt)
us = integrate.odeint(du_dt, usol0, ts)
timeind = np.linspace(0, Nt-1, int(Nt/1000), dtype=int)
for i in [timeind[-1]]:
    #plt.figure(0)
    plt.plot(x-c*ts[i],us[i, 0:N],label='$u$',zorder=-1);
    #plt.figure(1)
    plt.plot(x-c*ts[i],us[i, N:2*N],'--',label='$v$',zorder=-1);
# plt.figure(0)
# plt.xlabel('z')
# plt.ylabel('u,v');
# plt.figure(1)
# plt.xlabel('X')
# plt.ylabel('v');

# ax.plot(t, ladybirds, '--', label='ladybirds, $y(t)$\hspace{-14pt}', zorder=-3)

ax.set_xlim([-50, 30])
# ax.set_ylim([0, 1.2])

# plt.title('$c=1$',fontsize=12)


plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)


plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
