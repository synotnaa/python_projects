# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", True: 1} # !!! ключ должен быть неизменяемым типом данных и не повторяться
# print(d)
#
# key = 45
# del d[key]
# print(d)

# print(d[0])
# print(d[(1, 2.3)])
# print((1, 2.3) in d)
# d["ne"] = "Новое значение"
# print(d)
#
# for i in d: # тут получаем все ключи в словаре, ключи слева, их значения справа
#     print(i)
#
# for key in d:
#     print(key, ":", d[key])

# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")

# -----------------------------------------------------

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# count = 1
# for key in d:
#     count *= d[key]
# print(count)

# -----------------------------------------------------

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")

# d = {i: input("-> ") for i in range(1, 5)} # создаём словарь в одну строку циклом, с импутом значений и числовыми ключами
# print(d)
# dislike = int(input('Какой элемент вы хотите исключить? '))
# del d[dislike]
# print(d)

# -----------------------------------------------------

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб", sep="")

# -----------------------------------------------------

# d = {'a': 1, 'b':2, 'c':3}
# item = d.pop('w', 'Такого ключа не существует')
# print(item)
# print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# d = {'a': 1, 'b':2, 'c':3}
# d2 = {'r': 7, 'q': 9}
# # d3 = d.copy()
# # d3 = d.update(d2)
# d3 = d | d2
# print(d3)

#------------------------------------------

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

#------------------------------------------

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
#
# d['location'] = d.pop('city')
# print(d)

#------------------------------------------меняем ключи и значения местами

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # new_d = {value: key for key, value in d.items()}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

#------------------------------------------

sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
}

for x in sales:
    print(x)
    for y in sales[x]:
        print("\t", y, ":", sales[x][y])

person = input("Введите имя: ")
region = input("Регион: ")
print(sales[person][region])

new_data = int(input("Новое значение: "))
sales[person][region] = new_data
print(sales[person])

#дз 3:02:00

#------------------------------------------