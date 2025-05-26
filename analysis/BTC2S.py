import numpy as np
import matplotlib.pyplot as plt

# plt.figure(figsize=(6, 5))
ax = plt.subplot(1, 1, 1)

plot_flag = 3
# 1 for BTC; 2 for CTC; 3 for LPF
if plot_flag == 1:
    epsTF00 = [3.0, 4.4, 5.0, 5.5]
    epsTF05 = [3.6, 4.9, 5.5, 5.0]
    epsTF10 = [4.3, 5.6, 4.6, 3.7]
    epsTF15 = [5.4, 2.3, 1.8, 1.6]

    EB00 = [0.1, 0.1, 0.1, 0.2]
    EB05 = [0.2, 0.1, 0.1, 0.1]
    EB10 = [0.1, 0.1, 0.1, 0.2]
    EB15 = [0.2, 0.1, 0.2, 0.2]
if plot_flag == 2:
    epsTF00 = [1.3, 1.8, 2.5, 2.9]
    epsTF05 = [1.6, 2.2, 3.3, 5.4]
    epsTF10 = [2.0, 3.7, 6.8, 9.1]
    epsTF15 = [4.2, 21.0, 26.3, 27.4]

    EB00 = [0.1, 0.2, 0.1, 0.1]
    EB05 = [0.1, 0.1, 0.2, 0.1]
    EB10 = [0.1, 0.1, 0.1, 0.2]
    EB15 = [0.5, 1.2, 1.7, 1.4]
if plot_flag == 3:
    n_TF_max = 109
    epsTF00 = [x / n_TF_max * 100 for x in [4.4, 6.3, 8.1, 10.3]]
    epsTF05 = [x / n_TF_max * 100 for x in [5.2, 7.2, 10.2, 13.2]]
    epsTF10 = [x / n_TF_max * 100 for x in [6.8, 10.7, 18.4, 22.2]]
    epsTF15 = [x / n_TF_max * 100 for x in [10.8, 54.3, 61.6, 61.9]]

    EB00 = [x / n_TF_max * 100 for x in [0.1, 0.2, 0.2, 0.3]]
    EB05 = [x / n_TF_max * 100 for x in [0.3, 0.1, 0.2, 0.1]]
    EB10 = [x / n_TF_max * 100 for x in [0.3, 0.2, 0.2, 0.3]]
    EB15 = [x / n_TF_max * 100 for x in [1.0, 2.2, 2.6, 2.8]]

nTF = [200, 400, 600, 800]
epsTF = [0.0, 0.5, 1.0, 1.5]

colorNTF = ["#CD2626", "#FFA500", "#EEEE00", "#00c70f"][::-1]
markerETF = ['o', '^', 's', 'D']

data = [epsTF00, epsTF05, epsTF10, epsTF15]
errors = [EB00, EB05, EB10, EB15]

xi_values = [[n + 400 * eps - 800 for n in nTF] for eps in epsTF]

bars_data = []
for eps_idx, eps_data in enumerate(data):
    for n_idx, (xi, y_value) in enumerate(zip(xi_values[eps_idx], eps_data)):
        error_value = errors[eps_idx][n_idx]
        bars_data.append((xi, y_value, error_value, colorNTF[n_idx], markerETF[eps_idx]))

bars_data.sort(key=lambda x: x[0])

unique_xi = sorted(set(x[0] for x in bars_data))
bar_width = 0.22

for i, xi in enumerate(unique_xi):
    group = [bar for bar in bars_data if bar[0] == xi]
    for j, (xi, y_value, error_value, color, marker) in enumerate(group):
        x_pos = i + j * bar_width - (len(group) - 1) * bar_width / 2

        plt.errorbar(
            x_pos, y_value,
            yerr=error_value,
            fmt=marker,
            ecolor='black', color=color,
            elinewidth=5, capsize=10, markersize=15, markeredgecolor="black", markeredgewidth=1.5
        )

ticks_size = 22
plt.xticks(range(len(unique_xi)), [f"{xi:.0f}" for xi in unique_xi],
           fontproperties='Arial', size=ticks_size)

if plot_flag == 1:
    plt.ylim([0, 6])
    plt.yticks([0, 2, 4, 6], fontproperties='Arial', size=ticks_size)
    plt.ylabel("Bridge TF Count", fontproperties='Arial', size=25)
if plot_flag == 2:
    ax.set_yscale('log')
    plt.ylim([1, 40])
    plt.yticks([1, 10, 40], [1, 10, 40], fontproperties='Arial', size=ticks_size)
    ax.tick_params(axis='y', direction='in', which="minor", length=5, width=2)
    plt.ylabel("Competing TF Count", fontproperties='Arial', size=25)
if plot_flag == 3:
    ax.set_yscale('log')
    plt.ylim([1, 100])
    plt.yticks([1, 10, 100], [1, 10, 100], fontproperties='Arial', size=ticks_size)
    ax.tick_params(axis='y', direction='in', which="minor", length=5, width=2)
    plt.ylabel("Local Packing Fraction (%)", fontproperties='Arial', size=25)

ax.tick_params(axis='both', direction='in', which="major", length=8, width=2)
for spine in ax.spines.values():
    spine.set_linewidth(2)

plt.tight_layout(w_pad=1, h_pad=1)
plt.show()
