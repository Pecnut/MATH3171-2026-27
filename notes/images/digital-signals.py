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
t_max = 9.5
t = np.linspace(t_min,t_max,num=1000)
a_on = 3
a_off = 1
Dt = 2
x = np.ones(1000)*a_on
sl = [(t[i] // Dt) % 2 == 1 for i in range(len(x))]
sl = np.s_[sl]
x[sl] = a_off


fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.set_xticks([0, Dt,2*Dt,3*Dt,4*Dt,5*Dt])
ax.set_xticklabels(['$0$', '$\Delta t$', '$2\Delta t$',
                    '$3\Delta t$', '$4\Delta t$', '$5\Delta t$'])
ax.set_yticks([a_off,a_on])
ax.set_yticklabels(['$a_{\mathrm{off}}$','$a_{\mathrm{on}}$'])

ax.annotate('$t$', xy=(1, 0), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$a$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(t, x, zorder = -3)

ax.set_xlim([t_min, t_max*1.01])
ax.set_ylim(0,4)

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
