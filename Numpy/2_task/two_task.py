import numpy as np

def run_length_encoding(x):
    unique_values, fir_index = np.unique(x, return_index=True)
    counts = np.diff(np.concatenate((fir_index, [len(x)])))

    return unique_values, counts

# Пример
x = np.array([2, 2, 2, 3, 3, 3, 5])
result = run_length_encoding(x)
print(result)