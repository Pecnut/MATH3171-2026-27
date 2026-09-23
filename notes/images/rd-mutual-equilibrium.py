from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.special import erf

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

t_min = -2
t_max = 2
x = np.linspace(t_min,t_max,num=1000)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

# ax.set_xticks([-10,-5,-2.5,0,2.5,5,10])
# ax.set_xticklabels(['$-10$','$-5$','$-a$','$0$','$a$','$5$','$10$'])
# ax.set_yticks([0,A])
# ax.set_yticklabels([None,None])

ax.annotate('$x$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
#ax.annotate('$v$', xy=(0, 70), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#            textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


C2 = -0.1
w = 3/2*(np.tan(x/2+C2)**2+1)
w2 = 3/2*(np.tan(-x/2+C2)**2+1)
u = 0.5*3/2*(np.tan((x+0.4)/2+C2)**2+1)
v = w - u

#ax.plot(x, u, zorder = -3, label='$w(z)$',color='C2')
ax.plot(x, u, zorder = -3, label='$u$')
ax.plot(x, v, '--', zorder=-3, label='$v$')
#ax.plot(x, w, ':', zorder=-3, label='$w$')
#ax.plot(x, w2, ':', zorder=-3, label='$w$')

#ax.axvline(2,dashes=(1,2),linewidth=0.8,color='k')
#ax.axvline(-2,dashes=(1,2),linewidth=0.8,color='k')

ax.set_xlim([-2.1, 2.5])
#ax.set_ylim([0, 6])

plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)
plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
