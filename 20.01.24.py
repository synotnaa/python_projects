# num = 10
# num += 5
# print(num)
#
# num -=3
# print(num)

# num = 4321
# a = num % 10
# print("a:", a)
# num = num // 10
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print('c:', c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print(num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)
#
# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# print(int(2.5))
# print(round(2.501))
#
# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---", end="\n\n")
# print("Hello")

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print(res)

# print("Введите четыре числа: ")
# num1 = int(input("1: "))
# num2 = int(input("2: "))
# num3 = int(input("3: "))
# num4 = int(input("4: "))
# print("Результат: ", round((num1+num2)/(num3+num4), 2))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(0.0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print('privet' > 'PRIVET')
# print(ord('п'))

# print(5 - 3 == 2 and 1 + 3 == 4)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = input("Введите свой возраст: ")
# if int(age) >= 18:
#     print("Доступ разрешён ;)")
# else:
#     print("Доступ запрещён!")

# ...
# pass

# a = 15
# b = 15
# if a > b:
#     print('a>b')
# if b > a:
#     print('b>a')
# if a == b:
#     print('b=a')

# a = 15
# b = 15
# if a > b:
#     print('a>b')
# elif b > a:
#     print('b>a')
# else:
#     print('b=a')

a = int(input('Введите первую сторону: '))
b = int(input('Введите вторую сторону: '))
c = int(input('Введите третью сторону: '))
if a == b == c:
    print('Треугольник равносторонний')
elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')
