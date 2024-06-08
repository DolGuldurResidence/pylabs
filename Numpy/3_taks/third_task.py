import numpy as np

narray = np.random.randn(10,4)

print(f"Минимальное значение: {narray.min()}")
print(f"Максимальное значение: {narray.max()}")
print(f"Среднее значенеие: {narray.mean}")
print(f"Стандартное отклонение: {narray.std()}")
print(f"Первые пять строк:\n {narray[:5]}")