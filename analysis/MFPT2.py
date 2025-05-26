import numpy as np
import matplotlib.pyplot as plt

def FPT_GD(data, error_data, rev, Mshape, Tname, add_suffix=False):
    suffixes = [100, 200, 400, 600, 800]
    adjusted_GD = [1, 60, 200, 400]

    color_list = ["#CD2626", "#FFA500", "#EEEE00", "#00c70f", "#05b1ff", "#0f15ff"][::-1]

    reverse_flag = rev
    if reverse_flag:
        ticks = [10, 100, 1000]
        tick_labels = [-10, -100, -1000]
        mean_index = [2, 1, 0]
    else:
        ticks = [10, 100, 1000]
        tick_labels = [10, 100, 1000]
        mean_index = [3, 4, 5]

    plt.figure(figsize=(6, 8))
    ax = plt.subplot(1, 1, 1)

    if add_suffix:
        suffix0_data = np.array([])
        suffix0_error = np.array([])
        suffix0_means = [1] + [suffix0_data[i] for i in mean_index]
        suffix0_stds = [0] + [suffix0_error[i] for i in mean_index]
        plt.errorbar(
            adjusted_GD, suffix0_means, yerr=suffix0_stds,
            fmt='o-', color='gray', ecolor='black', elinewidth=5,
            capsize=15, markersize=20, markeredgecolor="black", markeredgewidth=1.5,
            linewidth=5, label="$n_{TF}$=0", zorder=3
        )

    for suffix_idx, (suffix, color) in enumerate(zip(suffixes, color_list[1:])):
        means = data[suffix_idx]
        stds = error_data[suffix_idx]
        plot_means = [1] + [means[i] for i in mean_index]
        plot_stds = [0] + [stds[i] for i in mean_index]

        plt.errorbar(
            adjusted_GD, plot_means, yerr=plot_stds,
            fmt=Mshape, color=color, ecolor='black', elinewidth=5,
            capsize=15, markersize=20, markeredgecolor="black", markeredgewidth=1.5,
            linewidth=5, label=f"$n_{{TF}}$={suffix}", zorder=3
        )

    # if reverse_flag:
    #     ax.text(0.88, 0.98, f"$\epsilon_{{TF}}={Tname}$",
    #             transform=ax.transAxes, ha='right', va='top', fontsize=32, fontfamily='Arial')

    plt.xlabel(r"$L_{E\text{-}P}$ (kb)", fontproperties='Arial', size=36)
    plt.ylabel(r"$\mathrm{MFPT}(\tau)$", fontproperties='Arial', size=38)

    ax.set_xscale('log')
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontproperties='Arial', size=32)
    ax.xaxis.set_tick_params(pad=7)
    ax.tick_params(axis='x', direction='in', which="major", length=10, width=2.5)
    ax.tick_params(axis='x', direction='in', which="minor", length=6, width=1.5)

    ax.set_ylim([0, 8000])
    y_major_ticks = [0, 2000, 4000, 6000, 8000]
    ax.set_yticks(y_major_ticks)
    ax.set_yticklabels(y_major_ticks, fontproperties='Arial', size=32)
    ax.set_yticks([1000, 3000, 5000, 7000], minor=True)
    ax.tick_params(axis='y', direction='in', which="major", length=10, width=2.5)
    ax.tick_params(axis='y', direction='in', which="minor", length=6, width=1.5)

    ax.set_xlim([10, 1000])
    for spine in ax.spines.values():
        spine.set_linewidth(2.5)
    if reverse_flag:
        ax.invert_xaxis()

    plt.grid(axis='y', alpha=0.66)
    plt.tight_layout()
    plt.show()


def FPT_GD_log(data, error_data, rev, Mshape, Tname, add_suffix=False):
    suffixes = [100, 200, 400, 600, 800]
    adjusted_GD = [1, 60, 200, 400]

    color_list = ["#CD2626", "#FFA500", "#EEEE00", "#00c70f", "#05b1ff", "#0f15ff"][::-1]

    reverse_flag = rev
    if reverse_flag:
        ticks = [10, 100, 1000]
        tick_labels = ['$-10^{1}$', '$-10^{2}$', '$-10^{3}$']
        mean_index = [2, 1, 0]
    else:
        ticks = [10, 100, 1000]
        tick_labels = ['$10^{1}$', '$10^{2}$', '$10^{3}$']
        mean_index = [3, 4, 5]

    plt.figure(figsize=(6, 8))
    ax = plt.subplot(1, 1, 1)

    # 绘制 suffix=0 时的 epsTF=0 的数据
    if add_suffix:
        suffix0_data = np.array([])
        suffix0_error = np.array([])
        suffix0_means = [1] + [suffix0_data[i] for i in mean_index]
        suffix0_stds = [0] + [suffix0_error[i] for i in mean_index]
        plt.errorbar(adjusted_GD, suffix0_means, yerr=suffix0_stds,
                     fmt='o', ecolor='black', color='gray', elinewidth=5,
                     capsize=15, markersize=20, markeredgecolor="black", markeredgewidth=1.5,
                     linewidth=5, label="$n_{TF}$=0", zorder=3)


    x = np.linspace(1, 1000, 10000)
    if rev == 1:
        if Tname == 0.0:
            y1 = 3 * x ** 1.30
            y2 = 3 * x ** 1.05
            ax.text(0.9, 0.9, "slope of 1.30",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.6, 0.09, "slope of 1.05",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')
        elif Tname == 0.5:
            y1 = 3 * x ** 1.15
            y2 = 3 * x ** 0.95
            ax.text(0.9, 0.9, "slope of 1.15",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.6, 0.09, "slope of 0.95",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=26, color='#6A5ACD')
        elif Tname == 1.0:
            y1 = 3 * x ** 1.10
            y2 = 3 * x ** 0.90
            ax.text(0.9, 0.9, "slope of 1.10",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.6, 0.09, "slope of 0.90",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')
        elif Tname == 1.5:
            y1 = 300 * x ** 0.55
            y2 = 3 * x ** 0.95
            ax.text(0.9, 0.97, "slope of 0.55",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='k')
            ax.text(0.6, 0.09, "slope of 0.95",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')

    if rev == 0:
        if Tname == 0.0:
            y1 = 5 * x ** 1.20
            y2 = 5 * x ** 0.95
            ax.text(0.6, 0.75, "slope of 1.20",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.97, 0.09, "slope of 0.95",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')
        elif Tname == 0.5:
            y1 = 5 * x ** 1.05
            y2 = 5 * x ** 0.85
            ax.text(0.6, 0.75, "slope of 1.05",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.97, 0.09, "slope of 0.85",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=26, color='#6A5ACD')
        elif Tname == 1.0:
            y1 = 5 * x ** 1.00
            y2 = 5 * x ** 0.80
            ax.text(0.6, 0.75, "slope of 1.00",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#EE6AA7')
            ax.text(0.97, 0.09, "slope of 0.80",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')
        elif Tname == 1.5:
            y1 = 300 * x ** 0.55
            y2 = 5 * x ** 0.90
            ax.text(0.6, 0.95, "slope of 0.55",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='k')
            ax.text(0.97, 0.09, "slope of 0.90",
                    transform=ax.transAxes, ha='right', va='top', fontfamily='Arial',
                    fontsize=28, color='#6A5ACD')


    if Tname == 1.5:
        plt.plot(x, y1, linewidth=2.5, zorder=2, color='k')
    else:
        plt.plot(x, y1, linewidth=2.5, zorder=2, color='#EE6AA7')
    plt.plot(x, y2, linewidth=2.5, zorder=2, color='#6A5ACD')

    for suffix_idx, (suffix, color) in enumerate(zip(suffixes, color_list[1:])):
        means = data[suffix_idx]
        stds = error_data[suffix_idx]
        plot_means = [1] + [means[i] for i in mean_index]
        plot_stds = [0] + [stds[i] for i in mean_index]

        plt.errorbar(
            adjusted_GD, plot_means, yerr=plot_stds,
            fmt=Mshape, ecolor='black', color=color,
            elinewidth=5, capsize=15, markersize=20,
            markeredgecolor="black", markeredgewidth=1.5,
            linewidth=5, label=f"$n_{{TF}}$={suffix}", zorder=3
        )

    # if reverse_flag:
    #     ax.text(0.88, 0.98, f"$\epsilon_{{TF}}={Tname}$",
    #             transform=ax.transAxes, ha='right', va='top', fontsize=32, fontfamily='Arial')

    plt.xlabel(r"$L_{E\text{-}P}$ (kb)", fontproperties='Arial', size=36)
    plt.ylabel(r"$\mathrm{MFPT}(\tau)$", fontproperties='Arial', size=38)

    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels, fontproperties='Arial', size=32)
    ax.xaxis.set_tick_params(pad=7)
    ax.tick_params(axis='x', direction='in', which="major", length=10, width=2.5)
    ax.tick_params(axis='x', direction='in', which="minor", length=6, width=1.5)


    ax.set_ylim([80, 10000])
    y_major_ticks = [100, 1000, 10000]
    ax.set_yticks(y_major_ticks)
    ax.set_yticklabels(['$10^{2}$', '$10^{3}$', '$10^{4}$'],
                       fontproperties='Arial', size=32)
    ax.tick_params(axis='y', direction='in', which="major", length=10, width=2.5)
    ax.tick_params(axis='y', direction='in', which="minor", length=6, width=1.5)

    ax.set_xlim([10, 1000])

    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    if reverse_flag:
        ax.invert_xaxis()

    plt.grid(axis='y', alpha=0.66, zorder=1)
    plt.tight_layout()
    plt.show()

epsTF = [0.0, 0.5, 1.0, 1.5]

log_flag = 0
if log_flag == 0:
    markers = ['o-', '^-', 's-', 'D-']
    for eps_index, (eps_data, eps_value, marker) in enumerate(zip(epsTF_data, epsTF, markers)):
        add_suffix0 = (eps_value == 0.0)
        if eps_index in [0, 1, 2, 3]:
            FPT_GD(eps_data, error_epsTF_data[eps_index], rev=0, Mshape=marker,
                   Tname=eps_value, add_suffix=add_suffix0)

if log_flag:
    markers = ['o', '^', 's', 'D']
    for eps_index, (eps_data, eps_value, marker) in enumerate(zip(epsTF_data, epsTF, markers)):
        add_suffix0 = (eps_value == 0.0)
        if eps_index in [0, 1, 2, 3]:
            FPT_GD_log(eps_data, error_epsTF_data[eps_index], rev=0, Mshape=marker,
                       Tname=eps_value, add_suffix=add_suffix0)
