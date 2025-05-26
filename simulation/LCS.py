import numpy as np
from sklearn.cluster import DBSCAN

fn=1  # for shell script to change
tab = [10000, 20000]
lcs_list = []
not_max_cluster_count = 0
total_ep_in_same_cluster = 0

with open(f'{fn}.pdb') as file:
    # For each configuration
    for i in range(tab[0], tab[1]):
        target_string = '{}'.format(i)
        data = []
        # Begin scanning
        for line in file:
            line_list = line.split()
            # If the first string in the line is 'MODEL' and the second string matches the target string
            if line_list[0] == 'MODEL' and line_list[1] == target_string:
                # Loop through each subsequent line until 'TER' is reached, and break the loop once find a model
                for next_line in file:
                    next_line_list = next_line.split()
                    # If 'TER' is reached, break out of the loop
                    if next_line_list[0] == 'TER':
                        break
                    # Otherwise, extract columns 6, 7, and 8 and convert them to floats
                    row = [float(next_line_list[i]) for i in range(5, 8)]
                    # Append the row to the data list
                    data.append(row)
                # Convert the data list to a numpy array
                data_array = np.array(data)
                # Because the unit of pdb file, 10^-10, is 10 times as much as the one in top file
                data_array /= 10
                # Save the E and P coordinates
                E_coor = data_array[246, :]
                P_coor = data_array[286, :]
                EP_coor = np.concatenate((E_coor, P_coor), axis=0)
                # Save the TF coordinates
                TF_array = data_array[533:]
                # E and P and TFs
                EPTF_array = np.concatenate((EP_coor, TF_array), axis=0)

                # DBSCAN clustering with a maximum distance of 1.8
                db = DBSCAN(eps=1.8, min_samples=1).fit(EPTF_array)
                # Labels represent different clusters. -1 indicates noise (no cluster)
                labels = db.labels_
                print('labels:', labels)

                # Find the size of the largest cluster
                unique_labels, counts = np.unique(labels, return_counts=True)
                print('unique_labels:', unique_labels)
                print('counts:', counts)

                max_cluster_size = counts.max()

                # Check if E and P are in the same cluster (i.e., same label)
                E_label = labels[0]
                P_label = labels[1]
                if E_label == P_label:  # E and P are in the same cluster
                    total_ep_in_same_cluster += 1
                    # Subtract 2 to exclude E and P from the count
                    cluster_size = counts[unique_labels == E_label][0] - 2
                    lcs_list.append(cluster_size)

                    # Check if the cluster containing E and P is not the largest
                    if cluster_size < max_cluster_size:
                        not_max_cluster_count += 1

                # Break the loop once the model is processed
                break

# Convert lcs_list to a numpy array and save it
lcs_array = np.array(lcs_list)
np.save(f'lcs{fn}.npy', lcs_array)

# Calculate the ratio of occurrences where E-P cluster is not the largest
if total_ep_in_same_cluster > 0:
    ratio = not_max_cluster_count / total_ep_in_same_cluster
else:
    ratio = 0

print(f'Total E and P in the same cluster: {total_ep_in_same_cluster}')
print(f'Number of cases where E-P cluster is not the largest: {not_max_cluster_count}')
print(f'Ratio of non-largest clusters to total E-P same cluster cases: {ratio:.2f}')











