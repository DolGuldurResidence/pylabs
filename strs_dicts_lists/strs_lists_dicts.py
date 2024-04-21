def compress_str(string):
    compressed_string = ""
    counter = 1
    for i in range(len(string)):
        if i != len(string) - 1 and string[i] == string[i + 1]:
            counter += 1
        else:
            if counter > 1:
                compressed_string += string[i] + str(counter)
            elif counter == 1:
                compressed_string += string[i]
            counter = 1
    return compressed_string


def decompress_string(compressed_string):
    decompressed_string = ""
    for i in range(0, len(compressed_string)):
        if compressed_string[i].isdigit():
            decompressed_string = decompressed_string + \
                                  compressed_string[i - 1] * (int(compressed_string[i]) - 1)
        else:
            decompressed_string = decompressed_string + compressed_string[i]
    return decompressed_string


def num_to_str(num):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
            'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот',
                'восемьсот', 'девятьсот']

    if 0 > num or num > 1000:
        return "Вы ввели неверное число"
    elif num == 1000:
        return "тысяча"
    else:
        string = ""
        num_str = str(num)
        num_list = [int(digit) for digit in num_str]

        if len(num_list) == 3:
            if num_list[1] == 1:
                string = hundreds[num_list[0]] + " " + teens[num_list[2]]
            else:
                string = hundreds[num_list[0]] + " " + tens[num_list[1] - 2] \
                         + " " + units[num_list[2]]
        elif len(num_list) == 2:
            if num_list[0] == 1:
                string = teens[num_list[1]]
            else:
                string = tens[num_list[0] - 2] + " " + units[num_list[1]]
        else:
            string = units[num_list[0]]

        return string


def count_strings(listok):
    counter = {}
    for i in listok:
        counter[i] = counter.get(i, 0) + 1

    for j in counter.values():
        print(j, end = ' ')


#задание №1
print(compress_str(input("Введите строку для сжатия")))

#задание №2
print(decompress_string(input("Введите строку для распоковки")))

#задание №3
print(num_to_str(int(input("Введите число для преобразования"))))

#задание №4
number = int(input("Введите количество строк, содержащихся в списке: "))
strings = [input(f"Введите {i + 1}-ую строку списка: ") for i in range(number)]
count_strings(strings)