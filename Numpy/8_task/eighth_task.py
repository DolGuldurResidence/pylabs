import numpy as np

array = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
notbublic_index = np.nonzero(array)[0]

print(notbublic_index)