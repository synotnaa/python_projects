# def add(a):
#     x = 2
#
#     def outer():
#         x = 3
#         print("x = ", x)
#         return a + x
#
#     return outer()
#
#
# print(add(5))

# --------------------------------------------------

# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#
#     inner()
#     print('a = ', a)
#     t = a
#
# fn()
# c = x + t
#
# print(c)

# --------------------------------------------------

# def fn1():
#     x = 25 # 2
#
#     def fn2():
#         x = 33 # 4 #55
#
#         def fn3():
#             nonlocal x
#             x = 55 # 6
#
#         fn3() # 5
#         print("fn2.x", x) # 7
#     fn2() #3
#     print("fn1.x", x) # 8
#
# fn1() #1

# --------------------------------------------------

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
# print(outer((2, 3, -1, 4))

# ________________замыкание_____________(возвращает ф-ю но не вызывает её)

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))
#
# print(outer(7)(10))
# def func(a):
#     return a * 2
#
# x = func(5)
# print(x)

# ----------------------------------------

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())

# ------------------------------------------

# def func(city):
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res2()

# ------------------------------------------

# lambda - выражение (аноним ф-ии)

# print((lambda x, y: x + y)(1, 2))
#
#
# def func(x, y):
#     return x + y
#
#
# # func = lambda x, y: x + y
# print(func(1,2))

# ------------------------------------------

# print((lambda a=1, b=2, c=3: a + b + c)())
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))

# ------------------------------------------

# c = (
#     lambda x: x*2,
#     lambda x: x*3,
#     lambda x: x*4,
# )
# for t in c:
#     print(t("abc_"))

# ------------------------------------------
# #1
# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
# #2
# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print(func2(5))
# #3
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))
#
# #4
# print((lambda n: (lambda x: n + x)) (10)(5))

# ------------------------------------------

# print((lambda n: (lambda x: (lambda z: n + x + z)))(10)(5)(1))

# ------------------------------------------

# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key = lambda i: i[1])
# lst = list(d.items())
# # print(lst)
# # lst.sort(key = lambda i: i[1])
# lst.sort(key = lambda i: i[1])
# print(lst)
# print(dict(lst))

# ------------------------------------------

# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семёнов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last_name'])
# print(res)
#
# res1 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res1)

# ------------------------------------------------------------------------------

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
# print(a[1](8,3))

# ------------------------------------------------------------------------------

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[6]()

# ------------------------------------------------------------------------------

# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius ** 2,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b)*h/2
# }
#
# print('Площадь окружности: ', area["Circle"](2))
# print('Площадь Rectangle: ', area["Rectangle"](10, 13))
# print('Площадь Trapezoid: ', area["Trapezoid"](7, 5, 3))

# ------------------------------------------------------------------------------

# print((lambda a, b: a if a > b else b)(5, 10))
# print((lambda a, b: a if a > b else b)(15, 10))

# ------------------------------------------------------------------------------
# dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_dz_

#------------------------------------------------------------------------------var1

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))

#var2

def outer(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s

s = outer(2,4,6)
s()
# outer(5,8,2)
# print(s)
# outer(1,6,8)
# print(s)

#------------------------------------------------------------------------------var3

# def outer(a, b, c):
#     s = 0
#     def inner(i, j):
#         nonlocal s
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))