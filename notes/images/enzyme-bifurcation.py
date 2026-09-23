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
t_max = 1.1
t = np.linspace(t_min, t_max, num=1000)
A = 1
a = 2
K = 1
#x = A*np.exp(a*t)
B = (1.7321*(27*t**2+1)**0.5+9*t)**(1/3)
x = 0.48075*B - 0.69336/B - t

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

# ax.set_xticks([0,0.333,1])
# ax.set_xticklabels([0,"$1/3$",1])
# ax.set_yticks([0,1/(3**1.5)])
# ax.set_yticklabels(["0","$3^{-3/2}$"])
ax.grid(True)
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$b$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$a$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x)

ax.set_xlim([t_min, t_max])
ax.set_ylim([0, 1.2/(3**1.5)])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
