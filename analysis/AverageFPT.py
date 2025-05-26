import numpy as np
import os

PATH_FPT = 'FPTdata/TFTF00'

k = [600, 800, 940, 60, 200, 400]
ntf_list = [0, 100, 200, 400, 800]

thr = 0.65
discard_len = 1000

averageFPT = np.full((len(ntf_list), len(k)), np.nan)
SE_FPT = np.full((len(ntf_list), len(k)), np.nan)

for j, gd in enumerate(k):
    print(f"GD of {gd}, nTF of {ntf_list}:")

    for i, ntf in enumerate(ntf_list):
        fpt = np.array([])

        for run in range(40):
            file_path = f'{PATH_FPT}/TF{ntf}GD{gd}FPT{run + 1}.npy'
            if os.path.exists(file_path):
                dis_array = np.load(file_path)

                if len(dis_array) > discard_len:
                    dis_array = dis_array[discard_len:]
                else:
                    continue

                max_90 = 0.9 * np.max(dis_array)
                index1_candidates = np.where(dis_array > max_90)[0]
                if len(index1_candidates) == 0:
                    continue
                index1 = index1_candidates[0]

                index2_candidates = np.where(dis_array[index1:] < thr)[0]
                if len(index2_candidates) == 0:
                    continue
                index2 = index1 + index2_candidates[0]

                fpt = np.append(fpt, index2 - index1)

        print(f"nTF of {ntf} Valid samples:", len(fpt))
        if len(fpt) > 0:
            averageFPT[i, j] = np.mean(fpt)
            SE_FPT[i, j] = np.std(fpt) / np.sqrt(len(fpt))

print("\nFinal Results:")
print("Average FPT:\n")
print(np.array2string(np.nan_to_num(averageFPT, nan=-1).astype(int),
                      separator=' ', threshold=np.inf).replace('[', ' ').replace(']', ' '))

print("\nSE of FPT:\n")
print(np.array2string(np.nan_to_num(SE_FPT, nan=-1).astype(int),
                      separator=' ', threshold=np.inf).replace('[', ' ').replace(']', ' '))

