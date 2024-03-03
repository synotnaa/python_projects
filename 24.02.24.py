# zip  - функция для создания кортежей
# a = ('dec', 'jan', 'feb')
# b = (12, 1, 2)
# c = (2.9, 3.7, 9.2)
# d = list(zip(b,))
# print(d)

# ----------------------------------------------------------------

# one = {'name': 'Igor', 'surname': 'Saint', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# ----------------------------------------------------------------

# lt = [('dec', 12), ('jan', 1), ('fev', 2)]
# a, b = zip(*lt)
# print(a)
# print(b)

# ----------------------------------------------------------------

# a = [1, 2, 3]
# b = [*a, 4, 5, 6] # звёздочкой квадратные скобки убираются, т.е. список мы прям напрямую добавляем в другой, без использования методов типа insert
# print(b)

# ----------------------------------------------------------------

# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'four': 4}
# print({**first, **second}) #звёздочку использовали как в примере выше, я как бы третий словарь создали новыми фигурными скобками. ** применяются к словарям, чтобы убрать фигурные скобки
# for k, v in {**first, **second}.items():
#     print(k, '->', v)

# ----------------------------------------------------------------

# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ')', color, sep='')
#     i +=1
#
# print()
#
# for num, val in enumerate(colors, start = 1):
#     print(num, ')', val, sep='')

# ----------------------------------------------------------------

# studs = {}
# n = int(input("Количество студентов: "))
#
# for i in range(n):
#     name = input(str(i + 1) + '-й студент:')
#     point = int(input('Введите балл: '))
#     studs[name] = point
#
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print(s)
# print('Средний бал: ', avg)
#
# for i in studs:
#     if studs[i] > avg:
#         print(i)

# ----------------------------------------------------------------

# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
# s = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(type(s))

# ----------------------------------------------------------------

# def func(a, *args):
#     return a, args
#
# print(func(5))

# def print_scors(student, *scores):
#     print("Student name:", student, end=", Оценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
# print_scors("Jonathan", 100, 96, 88, 92, 99, 84)
# print_scors("Rick", 96, 20, 33, 66)

# ----------------------------------------------------------------

# def func(*args, a):
#     return a, args
#
# print(func(5))
# print(func(1, 2, 3, 5, "abc")

# def func(**kwargs):
#     return kwargs
# print((func(a=1, b=2, c=3)))
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
# intro(name = "Irina", surname = "Smith", age = "23")
# intro(name = "Igor", surname = "Stone", email = "igor@gmail.com", country = "Russia", age = "23", phone = 9781600853)

# def func(a, b, *args, y = 0, **kwargs):
#     return a, b, args, kwargs, y
# print(func(5, 1, 2, 3, 4, 5, 6, 7, n = 9, m = 10, x = 5, y = 100))

# ----------------------------------------------------------------

# my_dict = {'one': 'first'}
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
# print("my_dict =", my_dict)
# db(k1 = 22, k2 = 31, k3 = 11, k4 = 91)
# print("my_dict = ", my_dict)
# db(name = 'Bob', age = 31, weight = 61, eyes_color = 'grey')
# print('mu_dict =', my_dict)

# ----------------------------------------------------------------

# name = 'Tom'
# surname = ''
# def hi():
#     surname = "Johnson"
#     global name, surname
#     name = 'Sam'
#     print('Hello', name, surname)
#
# def bye():
#     print('Good bye', name)
#
# hi()
# bye()
# print(name)
# print(surname)

#dz 16:27