import numpy as np
import matplotlib.pyplot as plt


def CP_GD(path, rev, Mshape, Tname):
    suffixes = [100, 200, 400, 600, 800]

    cpMean_dict = {"cpMean_0": np.load("./ConPro/cpMean_0.npy")}
    cpStd_dict = {"cpStd_0": np.load("./ConPro/cpStd_0.npy")}

    for suffix in suffixes:
        cpMean_dict[f"cpMean_{suffix}"] = np.load(f"{path}/cpMean_{suffix}.npy")
        cpStd_dict[f"cpStd_{suffix}"] = np.load(f"{path}/cpStd_{suffix}.npy")

    color_list = ["#CD2626", "#FFA500", "#EEEE00", "#00c70f", "#05b1ff", "#0f15ff"][::-1]

    # original_GD = [60, 200, 400, 600, 800, 940]
    adjusted_GD = [1, 60, 200, 400]

    reverse_flag = rev
    if reverse_flag:
        ticks = [10, 100, 1000]
        tick_labels = [-10, -100, -1000]
        mean_index = [5, 4, 3]
    else:
        ticks = [10, 100, 1000]
        tick_labels = [10, 100, 1000]
        mean_index = [0, 1, 2]

    new_point = {"mean": 0.8, "std": 0}

    plt.figure(figsize=(6, 8))
    ax = plt.subplot(1, 1, 1)

    for suffix, color in zip(suffixes, color_list[1:]):
        means = cpMean_dict[f"cpMean_{suffix}"]
        stds = cpStd_dict[f"cpStd_{suffix}"]

        plot_means = [means[i] for i in mean_index]
        plot_stds = [stds[i] for i in mean_index]

        plot_means.insert(0, new_point["mean"])
        plot_stds.insert(0, new_point["std"])

        p60, p200, p400 = plot_means[1], plot_means[2], plot_means[3]
        foldchange1 = p60 / p400
        foldchange2 = p200 / p400
        print(f'{foldchange1:.2f}, {foldchange2:.2f}')

        plt.errorbar(
            adjusted_GD, plot_means, yerr=plot_stds,
            fmt=Mshape, ecolor='black', color=color,
            elinewidth=5, capsize=15, markersize=20, markeredgecolor="black", markeredgewidth=1.5,
            linewidth=5, label=f"$n_{{TF}}$={suffix}", zorder=3
        )

        plt.plot(adjusted_GD, plot_means, '-', color=color, linewidth=5, zorder=2)

    if TextName == 0.0:
        means = cpMean_dict[f"cpMean_0"]
        stds = cpStd_dict[f"cpStd_0"]
        plot_means = [means[i] for i in mean_index]
        plot_stds = [stds[i] for i in mean_index]
        plot_means.insert(0, new_point["mean"])
        plot_stds.insert(0, new_point["std"])

        p60, p200, p400 = plot_means[1], plot_means[2], plot_means[3]
        foldchange1 = p60 / p400
        foldchange2 = p200 / p400
        print(f'{foldchange1:.2f}, {foldchange2:.2f}')
        plt.errorbar(
            adjusted_GD, plot_means, yerr=plot_stds,
            fmt=Mshape, ecolor='black', color='gray',
            elinewidth=5, capsize=15, markersize=20, markeredgecolor="black", markeredgewidth=1.5,
            linewidth=5, label=f"$n_{{TF}}$={suffix}", zorder=3
        )

        plt.plot(adjusted_GD, plot_means, '-', color='gray', linewidth=5, zorder=2)

    # if reverse_flag:
    #     ax.text(0.39, 0.98, f"$\epsilon_{{TF}}={Tname}$",
    #             transform=ax.transAxes, ha='right', va='top', fontsize=32, fontfamily='Arial')


    plt.xlabel(r"$L_{E\text{-}P}$ (kb)", fontproperties='Arial', size=36)
    plt.ylabel(r"$p_{E\text{-}P}$", fontproperties='Arial', size=38)
    plt.yticks([0.2 * x for x in range(1, 5)], fontproperties='Arial', size=32)

    # ax.set_yscale('log')
    ax.set_xscale('log')
    ax.tick_params(axis='both', direction='in', which="major", length=10, width=2.5)
    if not reverse_flag:
        ax.tick_params(axis='y', direction='in', which="major", length=0)
    ax.tick_params(axis='x', direction='in', which="minor", length=6, width=1.5)

    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontproperties='Arial', size=32)

    ax.set_ylim([0, 0.8])
    ax.set_xlim([10, 1000])

    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    if reverse_flag:
        ax.invert_xaxis()
    plt.grid(axis='y', alpha=0.66, zorder=1)
    plt.tight_layout()
    # plt.savefig(f'C:/Users/admin/Desktop/CPGD{Tname}.svg', transparent=True)
    plt.show()


epsTF = [0.0, 0.5, 1.0, 1.5]

for eps_index in range(4):

    if eps_index == 0:
        paTh = "./ConPro/015"
        MarkerShape = 'o'
    elif eps_index == 1:
        paTh = "./ConPro/TFTF05"
        MarkerShape = '^'
    elif eps_index == 2:
        paTh = "./ConPro/TFTF1"
        MarkerShape = 's'
    elif eps_index == 3:
        paTh = "./ConPro/TFTF15"
        MarkerShape = 'D'

    TextName = epsTF[eps_index]
    CP_GD(paTh, rev=0, Mshape=MarkerShape, Tname=TextName)
