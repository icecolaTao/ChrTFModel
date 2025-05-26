import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def EPcp3D():

    GD_index = 2  # GD: [60, 200, 400, 600, 800, 940]

    suffixes = [50, 100, 200, 400, 800]  # NTF

    cpMean_dict00 = {}
    cpMean_dict10 = {}
    cpMean_dict15 = {}

    file_name = "./ConPro/cpMean_0.npy"
    cpMean_dict00["cpMean_0"] = np.load(file_name)[GD_index]
    cpMean_dict10["cpMean_0"] = np.load(file_name)[GD_index]
    cpMean_dict15["cpMean_0"] = np.load(file_name)[GD_index]

    paTH = "./ConPro/015"
    for suffix in suffixes:
        file_name = f"{paTH}/cpMean_{suffix}.npy"
        cpMean_dict00[f"cpMean_{suffix}"] = np.load(file_name)[GD_index]

    paTH = "./ConPro/TFTF1"
    for suffix in suffixes:
        file_name = f"{paTH}/cpMean_{suffix}.npy"
        cpMean_dict10[f"cpMean_{suffix}"] = np.load(file_name)[GD_index]

    paTH = "./ConPro/TFTF15"
    for suffix in suffixes:
        file_name = f"{paTH}/cpMean_{suffix}.npy"
        cpMean_dict15[f"cpMean_{suffix}"] = np.load(file_name)[GD_index]

    epsilon_TF = [0.0, 1.0, 1.5]
    n_TF = [0, 50, 100, 200, 400, 800]
    cpMean_dicts = [cpMean_dict00, cpMean_dict10, cpMean_dict15]

    E, N = np.meshgrid(epsilon_TF, n_TF)
    cp_values = np.array(
        [[cpMean_dict[f"cpMean_{suffix}"] for suffix in [0] + suffixes] for cpMean_dict in cpMean_dicts]).T

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(E, N, cp_values, facecolor='#4169E1', edgecolor="#CD3333", alpha=0.8)

    ax.set_xticks([0.0, 1.0, 1.5], [0.0, 1.0,  1.5], fontproperties='Arial', size=12)
    ax.set_yticks([0, 100, 200, 400, 800], [0, 100, 200, 400, 800], fontproperties='Arial', size=12)
    ax.set_zticks([0.0, 0.2, 0.4, 0.6, 0.8], [0.0, 0.2, 0.4, 0.6, 0.8], fontproperties='Arial', size=12)
    ax.set_xlabel(r'$\epsilon_{TF}$', fontproperties='Arial', size=18)
    ax.set_ylabel(r'$n_{TF}$', fontproperties='Arial', size=18)
    ax.set_zlabel('E-P Contact Probability', fontproperties='Arial', size=12)
    ax.tick_params(axis='both', direction='in', length=5)
    plt.title("Gd=200kb", fontproperties='Arial', size=18)

    plt.show()

EPcp3D()