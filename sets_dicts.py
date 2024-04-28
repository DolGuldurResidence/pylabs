
#Задание №1
quantity = int(input("Введите количество элементов списка: "))
numbers = [int(input(f"Введите {i + 1} элемент списка: ")) for i in range(quantity)]
print(len(set(numbers)))



#Задание №2
quantity_1 = int(input("Введите количество элементов 1-го множества: "))
numbers_1 = set([int(input(f"Введите {i + 1} элемент 1-го мно-ва: ")) for i in range(quantity_1)])

quantity_2 = int(input("Введите количество элементов 2-го множества: "))
numbers_2 = set([int(input(f"Введите {i + 1} элемент 2-го мно-ва: ")) for i in range(quantity_2)])

if len(numbers_2) > len(numbers_1) and (numbers_2 & numbers_1) == numbers_1:
    print(True)
else:
    print(False)



#Задание №3
n = int(input("Введите максимальное кол-во городов: "))
cities = set()
i = 0

while i < n:
    city = input("Введите название города: ")
    if city not in cities:
        cities.add(city)
        print("OK")
        i += 1
    else:
        print("Ага, сжульничать решили?")



#задание №4
def pervious_count_words(string):
    words = string.split()
    used_words = []
    counter = []
    for i in words:
        if i in used_words:
            counter.append(used_words.count(i))
            used_words.append(i)
        else:
            used_words.append(i)
            counter.append(0)
    return counter

strochka = input("Введите произвольную строку")
print(pervious_count_words(strochka))



#Задание№5
def count_items_bought(n):
    purchases = {}

    for _ in range(n):
        entry = input("Введите запись о покупке в формате ID_Покупателя Товар Количество: ").split()
        customer_id, item, quantity = entry[0], entry[1], int(entry[2])

        if customer_id in purchases:
            purchases[customer_id].append((item, quantity))
        else:
            purchases[customer_id] = [(item, quantity)]

    for customer, items_bought in purchases.items():
        print(f"Покупатель {customer}:")
        for item, quantity in items_bought:
            print(f"Товар: {item}, Количество: {quantity}")

n = int(input("Введите количество записей о покупках: "))
count_items_bought(n)



#задание №6
def words_sorted_by_frequency(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count, key=lambda word: (-word_count[word], word))
    return sorted_words

text = input("Введите строку")
sorted_words = words_sorted_by_frequency(text)
for word in sorted_words:
    print(word)
