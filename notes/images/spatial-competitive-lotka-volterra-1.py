from __future__ import print_function, division
import os
from scipy import integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
# #rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

fig = plt.figure(figsize=(3*2./3*3., 2.2*2))
axes = fig.subplots(2, 3,sharey='row')
n = 0
for ax_i in range(2):
    for ax_j in range(3):
        n = ax_j + 1
        ax = axes[ax_i,ax_j]

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.tick_params(top=False, right=False)

        ticklabelpad_x = mpl.rcParams['xtick.major.pad']
        ticklabelpad_y = mpl.rcParams['ytick.major.pad']

        # if ax_i == 0:
        ax.set_xticks([-30,-10,10,30])
        #     ax.set_xticklabels(['$0$','$\pi/4$','$\pi/2$'])
        # else:
        #     ax.set_xticks([i*np.pi for i in [0, 1/2, 1]])
        #     ax.set_xticklabels(['$0$', '$\pi/2$', '$\pi$'])
        #ax.set_yticks([0,1])
        # ax.set_yticklabels([0,1])

        ax.annotate('$x$', xy=(40, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
                    xycoords='data', textcoords='offset points')
        # ax.annotate('$x$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
        #             xycoords='axes fraction', textcoords='offset points')

        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')

        path = os.path.dirname(os.path.abspath(__file__))
        data = np.genfromtxt(path+'/spatial-competitive-lotka-volterra-1-'+str(n)+'.csv',delimiter=',')

        x = data[0]
        u = data[1]
        v = data[2]
        dudt = data[3]
        dvdt = data[4]

        if ax_i == 0:
            ax.plot(x, u, label='$u$\hspace{-10pt}', zorder=3)
            ax.plot(x, v, '--', label='$v$\hspace{-10pt}', zorder=3)
        else:
            ax.plot(x, dudt, 
                    label='$\\frac{\partial u}{\partial t}$\hspace{-10pt}', zorder=3, color='C2')
            ax.plot(x, dvdt, '--',
                    label='$\\frac{\partial u}{\partial t}$\hspace{-10pt}', zorder=3, color='C3')

        max_x = max(x)*1.4
        ax.set_xlim([min(x), 40])
        if ax_i == 0:
            ax.set_ylim([0, 1.5])
        else:
            ax.set_ylim([-0.4, 0.4])

        if ax.is_last_col():
            ax.legend(ncol=1, frameon=False, framealpha=0,
                    borderpad=0, borderaxespad=0)
        
        if ax.is_first_row():
            ax.set_title('$t=' + ['0','10','100'][ax_j]  + '$',fontsize=12)

plt.tight_layout(pad=0.8, w_pad=1, h_pad=0.5)

#plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

# plt.figure(figsize=(3, 2.2))
# plt.plot(greenflies,ladybirds)

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

plt.show()
