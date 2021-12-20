import numpy as np
data = np.load('data/ex3_data.npy')
dropped_rows = np.count_nonzero(np.isnan(data).any(axis=1))
print(dropped_rows)
nan_in_col = np.count_nonzero(np.isnan(data), axis=0)
print(nan_in_col)