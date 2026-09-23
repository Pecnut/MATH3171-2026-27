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
L=1
#x = A*np.exp(a*t)
x1 = np.cos(2*np.pi*t/L)
x2 = np.cos(3*np.pi*t/L)

fig = plt.figure(figsize=(3,1.5))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0,L/2,L])
ax.set_xticklabels([0,'',"$L$"])
ax.set_yticks([-1,0,1])
ax.set_yticklabels(['$-1$','$0$','$1$'])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
# ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            # xycoords='axes fraction', textcoords='offset points')
# ax.annotate('$x$', xy=(0.5, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x1,'--',color='C0')
ax.plot(t, -x1, '--',color='C0')
ax.plot(t, x1*x2,color='C1')
plt.fill_between(t,x1*x2,color='C1',alpha=0.3)

ax.set_xlim([t_min, t_max])
ax.set_ylim([-1.1, 1.1])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.savefig('orthogonal-cos.pgf', transparent=True)

plt.show()
