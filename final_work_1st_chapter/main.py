import csv
import os
import random

def csv_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        list_data = list(reader)
    return list_data

def show(csv_list, output_type, num_rows=5, sepr='|'):
    if output_type == 'bottom':
        console_text = csv_list[-num_rows:]
    elif output_type == 'random':
        console_text = random.sample(csv_list, num_rows)
    else:
        console_text = csv_list[:num_rows]

    for row in console_text:
        print(sepr.join(row.values()))

def info(csv_list):
    header = csv_list[0]
    num_rows = len(csv_list) - 1
    num_columns = len(header)
    print(f"quantity of rows x columns: {num_rows}x{num_columns}")

    print("Field name\tQty\tType")
    for field in header:
        non_empty_count = sum(1 for row in data[1:] if row[field])
        field_type = type(data[1][field]).__name__
        print(f"{field}\t{non_empty_count}\t{field_type}")

def del_nan(list_csv):
    return [row for row in list_csv if all(row.values())]

def make_ds(data):
    learn= random.sample(data, int(0.7 * len(data)))
    test = [row for row in data if row not in learn]

    os.makedirs("workdata/Learning", exist_ok=True)
    os.makedirs("workdata/Testing", exist_ok=True)

    with open("workdata/Learning/train.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(learn)

    with open("workdata/Testing/test.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(test)




filename = "Titanic.csv"
data = csv_to_list(filename)
show(data, output_type='top', num_rows=5)
info(data)
data = del_nan(data)
make_ds(data)







