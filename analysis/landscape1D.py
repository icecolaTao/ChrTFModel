import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from scipy.signal import savgol_filter
import os


# -log(P) vs. contact p
def landscape_dx_03p(path, GD, tf_list, thr1, thr2, thr3, thr4,
                     draw=True, smooth=True, window_size=10):

    A_B = []
    saddle1_A = []
    saddle1_B = []
    B_C = []
    saddle2_B = []
    saddle2_C = []

    color_list = ["gray", "#0f15ff", "#05b1ff", "#00c70f", "#EEEE00", "#CD2626"]

    # color_list = ["#CD2626", "#FFA500", "#EEEE00", "#00c70f",
    #               "#0bdac0", "#05b1ff", "#0f15ff", "#9503fb"]

    if draw:
        plt.figure(figsize=(16, 8))

    for t in range(len(tf_list)):
        d = np.array([])
        ntf = tf_list[t]

        if ntf == 0:
            for i in range(30):
                if os.path.exists(f'./data/NewResults015/TF0GD{GD}dis{i + 1}.npy'):
                    d = np.append(d, np.load(f'./data/NewResults015/TF0GD{GD}dis{i + 1}.npy'))
        else:
            for i in range(30):
                if os.path.exists(f'{path}/TF{ntf}GD{GD}dis{i + 1}.npy'):
                    d = np.append(d, np.load(f'{path}/TF{ntf}GD{GD}dis{i + 1}.npy'))

        d = np.array(d)
        d = d[d < 13]

        # Yield cp using tanh
        cp = 1 / 2 * (1 + np.tanh(10 * (1 - d)))

        # Generate new reaction coordinate d*
        d_star = d - 5 * cp

        hist_values, bin_edges = np.histogram(d_star, bins=300, density=True)

        # # PROBABILITY PLOT
        # counts, bin_edges = np.histogram(d_star, bins=300)
        #
        # # Normalize the counts so that their sum is 1
        # counts_normalized = counts / counts.sum()
        # hist_values = counts_normalized

        x = bin_edges[:-1]
        index0 = np.where(hist_values == 0)  # np.where 返回的是一个元组的数组
        if len(index0[0]) > 0:  # Determines whether the array is empty.
            hist_values = hist_values[:index0[0][0]]
            negative_log_prob = -np.log(hist_values)
            y = negative_log_prob
            x = x[:index0[0][0]]
        else:
            negative_log_prob = -np.log(hist_values)
            y = negative_log_prob

        # Apply Savitzky-Golay filter to smooth the curve
        if smooth:
            y = savgol_filter(y, window_size, 3)

        # Find minimum and maximum values within the specified ranges
        min_range_1 = np.where(x <= thr1)
        max_range_1 = np.where((thr1 <= x) & (x <= thr2))
        min_range_2 = np.where((thr2 <= x) & (x <= thr3))
        max_range_2 = np.where((thr3 <= x) & (x <= thr4))
        min_range_3 = np.where((thr4 <= x))

        min_values_1 = np.argmin(y[min_range_1])

        # Align the minimums of state A with 0
        y_min_org = y[min_range_1][min_values_1]
        y -= y_min_org

        if draw:
            plt.plot(x, y, label=f'{ntf}', linewidth=3, color=color_list[t])
            plt.scatter(x[min_range_1][min_values_1], y[min_range_1][min_values_1],
                        color='red', s=40, zorder=3)

        # Sum and -log all the p whose x < x[min_range_1][min_values_1]
        hist_values = hist_values[:len(x)]
        real_A_value = - np.log(np.sum(hist_values[x < x[min_range_1][min_values_1]])) - y_min_org

        max_values_1 = np.argmax(y[max_range_1])
        # if draw:
        #     plt.scatter(x[max_range_1][max_values_1], y[max_range_1][max_values_1],
        #                 color='blue', s=40, zorder=3)

        min_values_2 = np.argmin(y[min_range_2])
        if draw and ntf not in [0, 400, 800]:
            plt.scatter(x[min_range_2][min_values_2], y[min_range_2][min_values_2],
                        color='red', s=40, zorder=3)

        max_values_2 = np.argmax(y[max_range_2])
        # if draw:
        #     plt.scatter(x[max_range_2][max_values_2], y[max_range_2][max_values_2],
        #                 color='blue', s=40, zorder=3)

        min_values_3 = np.argmin(y[min_range_3])
        if draw and ntf < 400:
            plt.scatter(x[min_range_3][min_values_3], y[min_range_3][min_values_3],
                        color='red', s=40, zorder=3)

        if ntf in [50, 100, 200, 400, 800]:
            # A: y[min_range_1][min_values_1] OR real_A_value
            A_B.append(y[min_range_1][min_values_1] - y[min_range_2][min_values_2])
            saddle1_A.append(y[max_range_1][max_values_1] - y[min_range_1][min_values_1])

            saddle1_B.append(y[max_range_1][max_values_1] - y[min_range_2][min_values_2])
            B_C.append(y[min_range_2][min_values_2] - y[min_range_3][min_values_3])
            saddle2_B.append(y[max_range_2][max_values_2] - y[min_range_2][min_values_2])
            saddle2_C.append(y[max_range_2][max_values_2] - y[min_range_3][min_values_3])

    if draw:
        ax = plt.subplot(1, 1, 1)
        plt.xticks(fontproperties='Arial', size=18)
        plt.yticks([-4, 0, 4, 8, 12], fontproperties='Arial', size=18)
        plt.xlabel(r'$\zeta = d - 5 \times cp$', fontproperties='Arial', size=24)
        plt.xlim([-5, 13])
        plt.ylabel(r'Free energy ($\epsilon$)', fontproperties='Arial', size=24)
        my_font = {'family': 'Arial', 'size': 18}
        plt.legend(frameon=False, prop=my_font, ncol=2)
        plt.title(f'{GD} kbp', fontproperties='Arial', size=24)
        ax.tick_params(axis='both', direction='in', length=6)
        # full-screen SVG
        # plt.savefig(f'C:/Users/admin/Desktop/LS{GD}.png', dpi=600)
        plt.show()

    return A_B, saddle1_A, saddle1_B, B_C, saddle2_B, saddle2_C


ntf_list = [0, 50, 100, 200, 400, 800]

GD = [60, 200, 400, 600, 800, 940]

pt = "./data/NewResultsTFTF15"
bt = "./BH/TFTF15"
os.makedirs(bt, exist_ok=True)

for k in GD:
    A_B, saddle1_A, saddle1_B, B_C, saddle2_B, saddle2_C = \
        landscape_dx_03p(pt, k, ntf_list, -4, 0, 1.45, 2.2, True, True)

    # np.save(f'{bt}/BH{k}_1.npy', A_B)
    # np.save(f'{bt}/BH{k}_2.npy', saddle1_A)
    # np.save(f'{bt}/BH{k}_3.npy', saddle1_B)
    # np.save(f'{bt}/BH{k}_4.npy', B_C)
    # np.save(f'{bt}/BH{k}_5.npy', saddle2_B)
    # np.save(f'{bt}/BH{k}_6.npy', saddle2_C)


# d: 1.1   cp: 0.1   zeta: 0.6
#    1.2       0.0         1.1
#    1.3       0.0         1.3
# d: 1.15 - 1.40 ~ state B
# d: < 0.8 ~ state A


def TEMP_BH_plot(BH):
    groups = ['50', '100', '200', '400', '800']
    categories = ['60', '200', '400', '600', '800', '940']

    if bt == "./BH/TFTF15":
        categories = ['200', '400', '600', '800']

    values = [[] for _ in groups]

    # Data for different BH differences
    for K in categories:
        temp = np.load(f'{bt}/BH{int(K)}_{BH}.npy')

        for i in range(len(groups)):
            values[i].append(temp[i])

    n_groups = len(groups)
    n_categories = len(categories)

    fig, ax = plt.subplots(figsize=(15, 8))

    bar_width = 0.12
    bar_positions = np.arange(n_groups)

    colors = ['#FF6666', '#FFB266', '#FFFF66', '#B2FF66', '#66B2FF', '#B266FF']
    colors = colors[1:]

    for i, category in enumerate(categories):
        ax.bar(bar_positions + i * bar_width, [values[j][i] for j in range(n_groups)], bar_width,
               color=to_rgba(colors[i], alpha=0.8), edgecolor='#363636', label=category)

    ax.set_xlabel(r'$n_{TF}$', fontproperties='Arial', size=24)
    ax.set_ylabel(r'Free energy $(\epsilon)$', fontproperties='Arial', size=22)
    ax.set_xticks(bar_positions + bar_width * (n_categories - 1) / 2)
    ax.set_xticklabels(groups, fontproperties='Arial', size=18)

    # Define y-ticks based on BH
    y_ticks_map = {
        1: ([6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [str(x) for x in [6, 5, 4, 3, 2, 1, 0, -1, -2, -3]]),
        2: ([0, 1, 2, 3, 4, 5, 6], ['0', '1', '2', '3', '4', '5', '6']),
        3: ([0, 1, 2, 3, 4, 5, 6, 7], ['0', '1', '2', '3', '4', '5', '6', '7']),
        4: ([1, 0, -1, -2, -3, -4, -5, -6], ['1', '0', '-1', '-2', '-3', '-4', '-5', '-6']),
        5: ([0, 1, 2, 3], ['0', '1', '2', '3']),
        6: ([0, 1, 2], ['0', '1', '2'])
    }

    if BH in y_ticks_map:
        ticks, labels = y_ticks_map[BH]
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels, fontproperties='Arial', size=18)

    if BH == 1:
        plt.ylim([-3, 6])

    ax.legend(title='Genomic distance (kbp)', title_fontsize='16',
              prop={'family': 'Arial', 'size': '16'}, ncol=2, frameon=False)

    ax.tick_params(axis='y', direction='in', which="major", length=5, right=True)
    ax.tick_params(axis='x', length=0)
    # plt.savefig('C:/Users/admin/Desktop/BH.png', dpi=600, transparent=True)
    plt.show()

# TEMP_BH_plot(3)
