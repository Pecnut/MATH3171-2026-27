from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

t_min = -1.2
t_max = 0.6
t = np.linspace(t_min,t_max,num=1000)
x = t**3+t**2

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

ax.annotate('$\lambda$', xy=(0.7, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='data', textcoords='offset points')
ax.annotate('$f(\lambda)$', xy=(0, 0.5), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='data', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x, zorder = -3)

ax.set_xlim([-1.2, 0.7])
ax.set_ylim([-0.3, 0.5])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
