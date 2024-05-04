import random
import json
import csv
import os
import sys

#запись файла
def write_file(file_path, string):
    try:
        with open(file_path, 'w') as file:
            file.write(string)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

#чтение файла
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Файл '{file_path}' не найден."
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {e}"

#запись строки в файл в колнку
def column_file(file_path,string):
    try:
        with open(file_path, 'w') as file:
            string = string.split()
            for i in string:
                file.write(str(i) + '\n')
    except Exception as e:
        print(f"Произошла ошибка при записи в файл в колнку: {e}")

#задача № 1
#запись случайных чисел в файл input.txt
random_nums = [str(random.randint(1, 100)) for i in range(10)]
random_nums = ' '.join(random_nums)
string_nums = write_file('first_task/input.txt', random_nums)

#основная часть задачи
product = 1
for i in read_file('first_task/input.txt').split():
    product = int(i) * product

write_file('first_task/output.txt', str(product))

#задача №2
#запись случайных чисел в somefile.txt
numbers = [str(random.randint(1,100)) for i in range(10)]
column_file('second_task/somefile.txt', ' '.join(numbers))

#основная часть задачи
file_numbers = read_file('second_task/somefile.txt')
file_numbers = file_numbers.split()
file_numbers = list(map(int, file_numbers))
file_numbers.sort()
file_numbers = list(map(str, file_numbers))
column_file('second_task/anotherfile.txt', ' '.join(file_numbers))

#Задача №3
with open('third_task/childrens.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

older = None
younger = None

for line in lines:
    parts = line.split()
    name = parts[0] + ' ' + parts[1]  
    age = int(parts[2])

    if older is None or age > int(older.split()[2]):  
        older = line

    if younger is None or age < int(younger.split()[2]): 
        younger = line

with open('third_task/older.txt', 'w', encoding='utf-8') as file:
    file.write(older)

with open('third_task/younger.txt', 'w', encoding='utf-8') as file:
    file.write(younger)

#задание №4
def json_to_csv(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    root_name = list(data.keys())[0]
    output_filename = f"{os.path.splitext(input_filename)[0]}_{root_name}.csv"

    with open(output_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        headers = list(data[root_name][0].keys())
        writer.writerow(headers)

        for item in data[root_name]:
            writer.writerow([item[header] for header in headers])

    print(f'Файл успешно преобразован. Результат сохранен в {output_filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
    else:
        json_filename = sys.argv[1]
        json_to_csv(json_filename)

json_to_csv('fourth_task/Sample-employee-JSON-data.json')
json_to_csv('fourth_task/Sample-JSON-file-with-multiple-records.json')