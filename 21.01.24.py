# crows = int(input('Введите число ворон на ветке: '))
# if 0 <= crows <= 9:
#     print("На ветке", end=" ")
#     if crows == 1:
#         print(crows, "ворона")
#     elif 2 <= crows <= 4:
#         print(crows, "вороны")
#     elif 5 <= crows <= 9 or crows == 0:
#         print(crows, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = input()

# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Такого значения не существует")

# day = 'четверг'
# time = 17
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 30
# print('a == b' if a == b else 'a > b' if a > b else 'b > a') # больше 3-х уровней вложенности лучше не делать, а то читаемость потеряется

# a, b = 20, 30
# print('на ноль делить нельзя' if b == 0 else round(a/b, 2))

# try:
#     n = int(input('Введите целое число: '))
#     print(n*2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки!')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError): # скобками тут создали кортеж (он как массив, но является 1 объектом
#     print('Нельзя вводить строки или нельзя делить на ноль!')
# else: # отработает когда в блоке try не возникло исключения
#     print('Всё нормально. Вы ввели числа', n, 'и', m)
# finally: # отработает в любом случае
#     print('Конец программы')


# n = input('Введите число 1: ')
# m = input('Введите число 2: ')
# try:
#     int(n)
#     int(m)
#     print(n + m)
# except (ValueError, NameError):
#     print(int(n) + int(m))

# Циклы

# i = 0
# while i <= 5:
#     print('i=', i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1
#
# n = int(input('Введите количество звёздочек: '))
# print(n * '*')
# print(n * '*\n')
# i = 0
# while i<n:
#     print('*')
#     i +=1
# while n > 0:
#     print('*')
#     n -= 1

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# summa = 0
# while a <= m:
#     if n % 2:
#         print(n, end=' ')
#         summa += n
#     n += 1
# print(sum)

# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершён')

# pr = 1
# while True:
#     a = int(input('Введите число: '))
#     if a == 0:
#         break
#     pr *= a
# print(pr)

# i = 0
# # while i < 10:
# #     if i == 5:
# #         break
# #     print(i)
# #     i += 1
# # else:
# #     print('Цикл окончен, i = ', i)

# dz 2:50