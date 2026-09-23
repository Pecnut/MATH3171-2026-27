from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import rc, cm
from scipy.special import erf
import matplotlib.tri as mtri
from matplotlib.colors import LightSource

rc('text', usetex=True)
#rc('text.latex', preamble=r'\usepackage[notextcomp]{stix2}')
rc('font', family='serif')
rc('font', size=12)

x_min = -50
x_max = 150
x = np.linspace(x_min,x_max,num=60)
t_min = 0
t_max = 50
t = np.linspace(t_min,t_max,num=60)

fig = plt.figure(figsize=(3,2.2))
ax = fig.gca(projection='3d')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(top=False, right=False)

ticklabelpad_x = mpl.rcParams['xtick.major.pad']
ticklabelpad_y = mpl.rcParams['ytick.major.pad']

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

def w(x,t):
    C = 1
    z = x - c*t
    return (1+C*np.exp(-z/np.sqrt(6)))**-2

c = 5/np.sqrt(6)

x, t = np.meshgrid(x, t)

# x = x.flatten()
# t = t.flatten()

# tri = mtri.Triangulation(x, t)

z = w(x,t)
rgb = np.ones((z.shape[0], z.shape[1], 3))
ls = LightSource(-10,-30)
# shade data, creating an rgb array.
#illuminated_surface = ls.shade_rgb(rgb, z)
illuminated_surface = ls.shade(z, cmap=cm.coolwarm)

green = np.array([0,1.0,0])
green_surface = ls.shade_rgb(rgb * green,z)
surf = ax.plot_surface(x, t, z, rstride=1, cstride=1, linewidth=0, 
                       antialiased=False, facecolors=illuminated_surface)

# u = 0.5*w(x+c*t)
# u = w(x+c*t)
# ax.plot(x, u, zorder = -3, label='$w(z)$',color='C2')
# surf = ax.plot_trisurf(x, t, w(x,t),linewidth=0, antialiased=False, cmap=cm.coolwarm)
#surf = ax.plot_surface(x, t, w(x,t))
    #ax.plot(x, u, zorder = -3, label='$u$')
    #ax.plot(x, v, '--', zorder=-3, label='$v$')

#ax.set_xlim([-12, 12])
#ax.set_ylim([0, 1.2])

ax.set_xlabel('$x$')
ax.set_ylabel('$t$')
ax.set_zlabel('$w$')

ax.view_init(30, -140)

#plt.legend(ncol=1, frameon=False, framealpha=0, borderpad=0, borderaxespad=0)
plt.subplots_adjust(right=1,top=1)
plt.show()
