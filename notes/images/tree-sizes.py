from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

# Import data from tree-sizes.csv
data = np.loadtxt('tree-sizes.csv', delimiter=',', skiprows=0)

t_min = 0.01
t_max = 10

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.tick_params(top=False, right=False)

#ax.set_xticks([0])
#ax.set_xticklabels([0])
#ax.set_yticks([0,A/(1+(A/K)),K])
#ax.set_yticklabels(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])
#ax.axhline(K,color='k',linewidth=0.8,dashes=(5,5),xmin=0.5)

# ticklabelpad_x = mpl.rcParams['xtick.major.pad']
# ticklabelpad_y = mpl.rcParams['ytick.major.pad']
# ax.annotate('$t$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')
# ax.annotate('$x$', xy=(0.5, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# log scatter plot
ax.set_xscale('log')
ax.set_yscale('log')
ax.scatter(data[:,1], data[:,0], s=2, color='C0')

ax.set_ylim([t_min, t_max])
ax.set_xlim([1, 200])

ax.set_ylabel(r'tree diameter (m)')
ax.set_xlabel(r'tree height (m)')

# Add a line with slope 2/3
x = np.linspace(t_min, t_max, 100)
y = 21 * x**(2/3)
ax.plot(y, x, '--', color='C1', label=r'$d \propto h^{3/2}$')
ax.legend(frameon=False, fontsize=10, loc='upper left')

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
