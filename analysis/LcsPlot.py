import numpy as np
import os
import matplotlib.pyplot as plt

def integ():
    lcs_integ = []

    path = './LcsSeries/PScontrol/TFTF15/400'
    for i in range(30):
        if os.path.exists(f"./{path}/lcs{i + 1}.npy"):
            temp = np.load(f"./{path}/lcs{i + 1}.npy")
            lcs_integ.append(temp)

    lcs_integ = np.vstack(lcs_integ)
    mean_values = np.mean(lcs_integ, axis=0)
    y = mean_values[1000: 11000]
    np.save('./LcsSeries/control15-400.npy', y)

# integ()

integ0 = np.load('LcsSeries/INTEG00-200-400.npy')
integ00 = np.load('LcsSeries/INTEG00-400-400.npy')
integ000 = np.load('LcsSeries/INTEG00-800-400.npy')
integ1 = np.load('LcsSeries/INTEG10-200-400.npy')
integ2 = np.load('LcsSeries/INTEG10-400-400.npy')
integ3 = np.load('LcsSeries/INTEG10-800-400.npy')
integ4 = np.load('LcsSeries/INTEG15-200-400.npy')
integ5 = np.load('LcsSeries/INTEG15-400-400.npy')
integ6 = np.load('LcsSeries/INTEG15-800-400.npy')

integctl1 = np.load('LcsSeries/control10-200.npy')
integctl2 = np.load('LcsSeries/control10-400.npy')
integctl3 = np.load('LcsSeries/control10-800.npy')
integctl4 = np.load('LcsSeries/control15-200.npy')
integctl5 = np.load('LcsSeries/control15-400.npy')
integctl6 = np.load('LcsSeries/control15-800.npy')

print(f'mean_lcs_00:', np.mean(integ0), np.mean(integ00), np.mean(integ000))
print(f'mean_lcs_10:', np.mean(integ1), np.mean(integ2), np.mean(integ3))
print(f'mean_lcs_15:', np.mean(integ4), np.mean(integ5), np.mean(integ6))
print(f'% of mean_lcs_00 in nTF:', 100*np.mean(integ0)/200,
      100*np.mean(integ00)/400, 100*np.mean(integ000)/800)
print(f'% of mean_lcs_10 in nTF:', 100*np.mean(integ1)/200,
      100*np.mean(integ2)/400, 100*np.mean(integ3)/800)
print(f'% of mean_lcs_15 in nTF:', 100*np.mean(integ4)/200,
      100*np.mean(integ5)/400, 100*np.mean(integ6)/800)

plot = 0
if plot:
    plt.figure(figsize=(15, 8))
    ax = plt.subplot(1, 1, 1)
    lineW = 1.25

    plt.plot(integ0, linewidth=lineW, color="#6495ED", label=r'$\epsilon=0, n_{TF}=200$')
    plt.plot(integ00, linewidth=lineW, color="#0000CD", label=r'$\epsilon=0, n_{TF}=400$')
    plt.plot(integ000, linewidth=lineW, color="#912CEE", label=r'$\epsilon=0, n_{TF}=800$')
    plt.plot(integ1, linewidth=lineW, color="#e9c46a", label=r'$\epsilon=1.0, n_{TF}=200$')
    plt.plot(integ2, linewidth=lineW, color="#f4a261", label=r'$\epsilon=1.0, n_{TF}=400$')
    plt.plot(integ3, linewidth=lineW, color="#e76f51", label=r'$\epsilon=1.0, n_{TF}=800$')
    plt.plot(integ4, linewidth=lineW, color="#98FB98", label=r'$\epsilon=1.5, n_{TF}=200$')
    plt.plot(integ5, linewidth=lineW, color="#2a9d8f", label=r'$\epsilon=1.5, n_{TF}=400$')
    plt.plot(integ6, linewidth=lineW, color="#556B2F", label=r'$\epsilon=1.5, n_{TF}=800$')

    my_font = {'family': 'Arial', 'size': 18}
    plt.legend(prop=my_font, frameon=False, ncol=3)
    plt.xlim([-100, 10100])

    zoom_in = 1
    if zoom_in:
        plt.ylim([0, 100])
        plt.yticks([25 * x for x in range(7)] + [5 * x for x in range(5)],
                   fontproperties='Arial', size=15)
    else:
        plt.ylim([0, 800])
        plt.yticks([100*x for x in range(9)], fontproperties='Arial', size=15)

    plt.xticks([2000*x for x in range(6)], fontproperties='Arial', size=15)
    plt.ylabel("TFs in the largest cluster",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.xlabel(r"Simulation time ($\tau$)",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.title("Gd=400kb, averaged over 30 trajectories", fontproperties='Arial', size=18)
    ax.tick_params(axis='y', direction='in')
    ax.tick_params(axis='x', length=0)
    # plt.savefig('C:/Users/admin/Desktop/lcs1.png', dpi=600, transparent=True)
    plt.show()


plt.figure(figsize=(15, 8))
ax = plt.subplot(1, 1, 1)
lineW = 1.25
TFTF = 1.5

if TFTF == 1:
    plt.plot(integctl1, linewidth=lineW, color="k", label=r'$control-200$')
    plt.plot(integctl2, linewidth=lineW, color="#2F4F4F", label=r'$control-400$')
    plt.plot(integctl3, linewidth=lineW, color="#8B658B", label=r'$control-800$')
    plt.plot(integ1, linewidth=lineW, color="#e9c46a", label=r'$\epsilon=1.0, n_{TF}=200$')
    plt.plot(integ2, linewidth=lineW, color="#f4a261", label=r'$\epsilon=1.0, n_{TF}=400$')
    plt.plot(integ3, linewidth=lineW, color="#e76f51", label=r'$\epsilon=1.0, n_{TF}=800$')

    my_font = {'family': 'Arial', 'size': 18}
    plt.legend(prop=my_font, frameon=False, ncol=2)
    plt.xlim([-100, 10100])
    plt.ylim([0, 100])
    plt.yticks([20 * x for x in range(6)], fontproperties='Arial', size=15)

    plt.xticks([2000 * x for x in range(6)], fontproperties='Arial', size=15)
    plt.ylabel("TFs in the largest cluster",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.xlabel(r"Simulation time ($\tau$)",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.title("Gd=400kb, averaged over 30 trajectories", fontproperties='Arial', size=18)
    ax.tick_params(axis='y', direction='in')
    ax.tick_params(axis='x', length=0)

    # plt.savefig('C:/Users/admin/Desktop/LcsCtl1.png', dpi=600, transparent=True)
    plt.show()

if TFTF == 1.5:
    plt.plot(integctl4, linewidth=lineW, color="k", label=r'$control-200$')
    plt.plot(integctl5, linewidth=lineW, color="#4682B4", label=r'$control-400$')
    plt.plot(integctl6, linewidth=lineW, color="#191970", label=r'$control-800$')
    plt.plot(integ4, linewidth=lineW, color="#98FB98", label=r'$\epsilon=1.5, n_{TF}=200$')
    plt.plot(integ5, linewidth=lineW, color="#2a9d8f", label=r'$\epsilon=1.5, n_{TF}=400$')
    plt.plot(integ6, linewidth=lineW, color="#556B2F", label=r'$\epsilon=1.5, n_{TF}=800$')

    my_font = {'family': 'Arial', 'size': 18}
    plt.legend(prop=my_font, frameon=False, ncol=2)
    plt.xlim([-100, 10100])
    plt.ylim([0, 800])
    plt.yticks([100 * x for x in range(9)], fontproperties='Arial', size=15)

    plt.xticks([2000 * x for x in range(6)], fontproperties='Arial', size=15)
    plt.ylabel("TFs in the largest cluster",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.xlabel(r"Simulation time ($\tau$)",
               fontproperties='Arial', size=18, labelpad=-1)
    plt.title("Gd=400kb, averaged over 30 trajectories", fontproperties='Arial', size=18)
    ax.tick_params(axis='y', direction='in')
    ax.tick_params(axis='x', length=0)

    # plt.savefig('C:/Users/admin/Desktop/LcsCtl2.png', dpi=600, transparent=True)
    plt.show()
