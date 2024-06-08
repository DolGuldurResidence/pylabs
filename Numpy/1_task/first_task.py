import numpy as np



text = '''1.	Сохранить этот текст в файл. Прочитать матрицу из файла. Hайдите для этой матрицы сумму всех элементов, максимальный и минимальный элемент (число)
3,4,17,-3,5,11,-1,6,0,2,-5,8'''

with open('1_task/first_task.txt', 'w', encoding='UTF-8') as file:
    file.write(text)

with open('1_task/first_task.txt', 'r') as file:
    lines = file.readlines()[1:]

numbers = [list(map(int, line.strip().split(','))) for line in lines]

matrix = np.array(numbers)
matrix = matrix.reshape(3, 4)

print(np.sum(matrix))
print(np.max(matrix))
print(np.min(matrix))