from __future__ import print_function, division
from scipy import integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
# #rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

fig = plt.figure(figsize=(3,2.2))
ax = fig.subplots(1, 1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)
#ax.axis('equal')

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.annotate('$\lambda$', xy=(1, 0.5), xytext=(0, -2*ticklabelpad_x), ha='right', va='top',
            xycoords='axes fraction', textcoords='offset points')
# ax.annotate('$v$', xy=(0, 1), xytext=(-2*ticklabelpad_y, 0), ha='right', va='top',
#             xycoords='axes fraction', textcoords='offset points')

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# ax.set_ylim([0, 1.6])
# ax.set_xlim([0, 1.6])

# plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

alpha1 = 0.0
alpha2 = 0.2
alpha3 = 0.4
beta = 0.4
c = (4*alpha2*(1 - beta))**0.5;
lam = np.linspace(-1.5,1.5,100);
p1 = lam**3 + lam**2*(c - beta/c) - beta*lam - beta*alpha1*(beta - 1)/c;
p2 = lam**3 + lam**2*(c - beta/c) - beta*lam - beta*alpha2*(beta - 1)/c;
p3 = lam**3 + lam**2*(c - beta/c) - beta*lam - beta*alpha3*(beta - 1)/c;

ax.set_xticks([0,-c,beta/c])
ax.set_xticklabels([0,'$-c$','$\\beta/c$'])
ax.set_yticks([0])
ax.set_yticklabels([0])

plt.plot(lam, p1)
plt.plot(lam, p2)
plt.plot(lam, p3)
# plt.plot(lam,0*lam,'k--')
# plt.ylabel('p')
# plt.xlabel('$\lambda$');
plt.ylim(-0.5,0.5);

plt.tight_layout(pad=0.2, w_pad=0, h_pad=0)


plt.show()
