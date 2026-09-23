from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

t_min = -3
t_max = 3
t = np.linspace(t_min,t_max,num=1000)
A = 1
a = 0.9
x = A*np.exp(a*t)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.set_xticks([0])
ax.set_xticklabels([0])
ax.set_yticks([0,A])
ax.set_yticklabels([None,None])
ax.annotate('$A$', xy=(0.5, 0.14), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')


ax.annotate('$t$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$x$', xy=(0.5, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x, zorder = -3)

ax.set_xlim([t_min, t_max*1.01])
ax.set_ylim([0, None])

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
