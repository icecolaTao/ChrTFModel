import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy.optimize import curve_fit


def preprocessing_CMT(NTF, paTH):

    ntf = NTF
    GD = [60, 200, 400, 600, 800, 940]

    CMT_mean = np.array([])
    CMT_std = np.array([])

    for k in GD:
        CMT_number = np.array([])
        for i in range(30):
            if os.path.exists(f'{paTH}/TF{ntf}GD{k}LCS{i + 1}.npy'):
                temp = np.load(f'{paTH}/TF{ntf}GD{k}LCS{i + 1}.npy')
                temp_corrected = np.mean(temp) * len(temp) / 12500
                CMT_number = np.append(CMT_number, temp_corrected)

        CMT_mean = np.append(CMT_mean, np.mean(CMT_number))
        CMT_std = np.append(CMT_std, np.std(CMT_number))

    return ntf, CMT_mean, CMT_std

pt = "./data/NewResults015"
st = "./CMT/TFTF0"
os.makedirs(st, exist_ok=True)

save_flag = 0
if save_flag:
    for t in [50, 100, 200, 400, 800]:
        nTF, CMT_mean, CMT_std = preprocessing_CMT(t, pt)
        np.save(f"{st}/cmtMean_{nTF}", CMT_mean)
        np.save(f"{st}/cmtStd_{nTF}", CMT_std)


plot_flag = 1
if plot_flag:
    plt.figure(figsize=(11, 7))
    ax = plt.subplot(1, 1, 1)
    color_list = ['#FF8247', '#458B00', '#0000CD',
                  '#9B30FF', '#00FF7F', '#FF3030']

    for GD_index, zorder_index in zip([0, 5, 1, 4, 2, 3], [5, 6, 3, 4, 1, 2]):
        # original: GD_list = [60, 200, 400, 600, 800, 940], zorder = [5, 3, 1, 2, 4, 6]
        GD_list = [60, 200, 400, -400, -200, -60]
        GD = GD_list[GD_index]

        cp = np.array([])
        cmt = np.array([])

        path3 = "./ConPro/TFTF1"
        path4 = "./CMT/TFTF1"
        for t_index in [50, 100, 200, 400, 800]:
            temp1 = np.load(f'{path3}/cpMean_{t_index}.npy')
            temp2 = np.load(f'{path4}/cmtMean_{t_index}.npy')
            cp = np.append(cp, temp1[GD_index])
            cmt = np.append(cmt, temp2[GD_index])


        variable = cmt

        plt.scatter(variable, cp, marker='s', edgecolor="black", linewidth=1,
                    s=267, alpha=1, color=color_list[GD_index], zorder=zorder_index+6)

        fit_flag = 0
        if fit_flag:
            func = 'hill'  # gaussian, hill

            if func == 'gaussian':
                def gaussian(x, amplitude, mean, stddev):
                    return amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))

                from scipy.special import gamma
                def gamma_func(x, A, k, theta):
                    return A * (x ** (k - 1) * np.exp(-x / theta)) / (theta ** k * gamma(k))

                x = variable
                y = cp

                A_guess = 16
                # Peak Position = θ(k−1)
                k_guess = 2.0
                theta_guess = 10.0

                initial_guess = [A_guess, k_guess, theta_guess]
                params, covariance = curve_fit(gamma_func, x, y, p0=initial_guess)
                A_fit, k_fit, theta_fit = params

                x_fit = np.linspace(0, 600, 3000)
                y_fit = gamma_func(x_fit, A_fit, k_fit, theta_fit)

                plt.plot(x_fit, y_fit, linewidth=4, label=f"$L_{{E\\text{{-}}P}}={GD}$ kb",
                         color=color_list[GD_index], zorder=zorder_index)


            if func == 'hill':
                def hill_function(x, P0, Pmax, n, K):
                    return P0 + Pmax * x ** n / (K ** n + x ** n)

                x = variable
                y = cp

                initial_guess = [0, 0.8, 1.5, 2.5]  # Initial guess for n and K
                popt, pcov = curve_fit(hill_function, x, y, p0=initial_guess)

                P0_fit, Pmax_fit, n_fit, K_fit = popt

                x_fit = np.linspace(0, 600, 3000)
                y_fit = hill_function(x_fit, P0_fit, Pmax_fit, n_fit, K_fit)

                plt.plot(x_fit, y_fit, linewidth=4,
                         color=color_list[GD_index], zorder=zorder_index)
                print(f'P0:{P0_fit:.2f}, Pmax:{Pmax_fit:.2f}, n:{n_fit:.2f}, K:{K_fit:.2f}')

    plt.ylim([0, 0.8])
    plt.xlim([0.2, 700])
    ax.set_xscale('log')

    plt.xticks([1, 10, 100, 600], [1, 10, 100, 600], fontproperties='Arial', size=24)
    plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8], fontproperties='Arial', size=24)
    plt.xlabel(r'$n_{TF}^{E\text{-}P}$', fontproperties='Arial', labelpad=-5, size=30)
    plt.ylabel(r'$p_{E\text{-}P}$', fontproperties='Arial', size=30)

    my_font = {'family': 'Arial', 'size': 15}
    # plt.legend(prop=my_font, frameon=False, loc="upper center", ncol=3)

    ax.tick_params(axis='both', direction='in', width=2, length=9)
    ax.tick_params(axis='x', which='minor', direction='in', width=2, length=5)

    for spine in ax.spines.values():
        spine.set_linewidth(2)

    # if fit_flag:
    #     plt.title(r'Data points fitted with Gamma-pdf-like function '
    #               r'$\frac{A x^{k-1} e^{-x / \theta}}{\theta^k \Gamma(k)}$',
    #               fontproperties='Arial', size=14)

    # # zoom-in for large size at 1.5
    # plt.xlim([450, 600])
    # plt.ylim([-0.01, 0.2])
    # plt.xticks([450, 500, 550, 600], fontproperties='Arial', size=16)
    # plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], fontproperties='Arial', size=16)

    # plt.savefig(f'C:/Users/admin/Desktop/ALLGd.png', dpi=600)
    plt.show()


