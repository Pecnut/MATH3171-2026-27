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
x = np.linspace(t_min,t_max,num=1000)
L = 1
b = 0.01
# b = 1*(np.pi/L)**2#20

N = 30
C0 = [1/L]
Cnpositive = [2/L*np.sin(n*np.pi/2) for n in range(1,N)]
Cn = C0 + Cnpositive

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

# ax.set_xticks([0])
# ax.set_xticklabels([0])
# ax.set_yticks([0,A])
# ax.set_yticklabels([None,None])

ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$u$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

for t in [0.001, 0.005, 0.03, 10.1]:
    u = np.sum([Cn[n]*np.exp((-(n*np.pi/L)**2+b)*t)*np.sin(n*np.pi*x/L) for n in range(len(Cn))],axis=0)
    ax.plot(x, u, zorder = -3, label='$t=' + str(t) + '$')

ax.set_xlim([t_min, t_max*1.1])
ax.set_ylim([0, None])

plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)
plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
