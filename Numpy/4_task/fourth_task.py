import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

bublik_index = np.where(x == 0)[0]

y = []
for i in range(len(bublik_index)):
    if i + 1 < len(bublik_index):
        y.append(x[bublik_index[i]+1])

y = np.array(y)

print(f"Максимальное значение:{y.max()}")
