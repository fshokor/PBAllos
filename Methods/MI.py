# inspired from https://stackoverflow.com/questions/20491028/optimal-way-to-compute-pairwise-mutual-information-using-numpy
import pandas as pd
import numpy as np
import os

import matplotlib.pylab as plt
import seaborn as sns

# Mutual information
def calc_MI(X, Y, bins):

   c_XY = np.histogram2d(X, Y, bins)[0]
   c_X = np.histogram(X, bins)[0]
   c_Y = np.histogram(Y, bins)[0]

   H_X = shan_entropy(c_X)
   H_Y = shan_entropy(c_Y)
   H_XY = shan_entropy(c_XY)

   MI = H_X + H_Y - H_XY
   return MI
   
# shannon entropy 
def shan_entropy(c):
    c_normalized = c / float(np.sum(c))
    c_normalized = c_normalized[np.nonzero(c_normalized)]
    H = -sum(c_normalized * np.log(c_normalized))
    return H


def MI_matrix(input_path=None, output_dir=None, start_idx=None, end_idx=None, data_size=None ):
    """
    compute mutual information between columns/positions and generate a matrix
    Args:
        input_path: path to sequences array input file
        output_dir: path to output directory
        start_idx: index of first row/sequence
        end_idx: index of last row/sequence

    """
    bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    k = np.load(input_path)
    for i in range(start_idx, end_idx, data_size):
        k = k[start_idx:start_idx+data_size, :]
        r = k.shape[1]
        matMI = np.zeros((r, r))

        for ix in np.arange(r):
                for jx in np.arange(ix+1, r):
                    matMI[ix, jx] = calc_MI(k[:, ix], k[:, jx], bins)
                    matMI[jx, ix] = calc_MI(k[:, ix], k[:, jx], bins)

        npy_file = 'matMI{0}.npy'.format(i+1)
        output_path = os.path.join(output_dir,  npy_file)
        np.save(output_path, matMI)

        csv_file = 'matMI{0}.csv'.format(i+1)
        output_path = os.path.join(output_dir, csv_file)
        df3 = pd.DataFrame(matMI)
        df3.to_csv(output_path)




