from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ax.set_xticks([0,50,100,150])
# ax.set_xticklabels([0,"$a$","$b$","$c$","$k$"])
# ax.set_yticks([0,R])#0,A/(1+(A/K)),K])
# ax.set_yticklabels([0,"$R$"])#(["0","$\\textstyle\\frac{A}{1+A/K}$","$K$"])


x = np.linspace(1.005,100,10000)
R = 2*x**3/(1 + x**2)**2;
k = 2*x**3/(x**2 - 1)
#plt.rcParams.update({'font.size': 14}) # increase the font size plt.xlabel("k")
#plt.ylabel("R")
plt.plot(k,R);
plt.ylim(-0.2,0.7)
plt.xlim(0,200);
plt.text(75, 0.6, "\\textbf{1 equilibrium}")
plt.text(75, 0.3, "\\textbf{3 equilibria}")
plt.text(75, -0.2, "\\textbf{1 equilibrium}");


ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']
ax.annotate('$k$', xy=(1, 0.23), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
ax.annotate('$R$', xy=(0.00, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
             xycoords='axes fraction', textcoords='offset points')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)
plt.show()
