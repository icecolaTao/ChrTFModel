import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import os
from matplotlib import cm
from matplotlib.colors import ListedColormap


def landscape_3D(route, paTH):
    d = np.array([])
    for i in range(30):
        if os.path.exists(f'data/{route}/{paTH}dis{i + 1}.npy'):
            d = np.append(d, np.load(f'data/{route}/{paTH}dis{i + 1}.npy'))
    d = np.array(d)
    d = d[d < 15]
    cp = 1 / 2 * (1 + np.tanh(10 * (1 - d)))

    data_2D = np.zeros([2, len(d)])
    data_2D[0] = d
    data_2D[1] = cp

    return data_2D

# 0.0-400, 1.0-400, 1.5-400
path00 = 'NewResults015'
path01 = 'NewResultsTFTF1'
path02 = 'NewResultsTFTF15'

path1 = "TF200GD400"
path2 = "TF400GD400"
path3 = "TF800GD400"

path1 = "TF200GD200"
path2 = "TF400GD200"
path3 = "TF800GD200"

PATH0 = path02
PATH = path2

data = landscape_3D(PATH0, PATH)
kde = gaussian_kde(data)
x, y = np.meshgrid(np.linspace(data[0].min(), data[0].max(), 500),
                   np.linspace(data[1].min(), data[1].max(), 500))
grid_coords = np.vstack([x.ravel(), y.ravel()])

save_fig = 0
if save_fig:
    z = kde(grid_coords).reshape(x.shape)
    z[z < 0.000001] = 0.000001
    logz = - np.log(z)
    np.save(f"./landscape/{PATH0}-{PATH}.npy", logz)
else:
    logz = np.load(f"./landscape/{PATH0}-{PATH}.npy")

logz[logz > 6] = 6
print("logz.min:", np.min(logz), "logz.max:", np.max(logz))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cmp_modified = cm.get_cmap('plasma', 256)
custom_cmp = ListedColormap(cmp_modified(np.linspace(0., 0.95, 256)))

surf = ax.plot_surface(x, y, logz, cmap=custom_cmp,
                       rstride=1, cstride=1, vmin=-1, vmax=6)
contour = ax.contour(x, y, logz, zdir='z', levels=20, linewidths=1,
                     offset=-3.5, cmap=custom_cmp, vmin=-3.5, vmax=6.5)

cbar = fig.colorbar(surf, ax=ax, shrink=0.67, aspect=14)
cbar.set_ticks([-1, 2.5, 6])
cbar.set_ticklabels(['0', '5', '10'], fontproperties='Arial', size=12)
cbar.ax.tick_params(which='both', direction='in', length=4, width=1)
cbar.ax.yaxis.set_ticks_position('both')

plt.xticks([0.4 * 8 * x for x in range(5)], [str(8 * x) for x in range(5)],
           fontproperties='Arial', size=12)
plt.yticks(fontproperties='Arial', size=12)
ax.set_zticks([-3.5, 1.5, 6.5], ['0', '5', '10'], fontproperties='Arial', size=12)

ax.set_xlim(0, 13)
ax.set_ylim(0, 1)
ax.set_zlim([-3.5, 6.5])

ax.grid(False)
ax.set_box_aspect((10, 11, (ax.get_zlim()[1]-ax.get_zlim()[0])))
ax.view_init(elev=25, azim=-140)
plt.show()