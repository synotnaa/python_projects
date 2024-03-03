a = 5
b = 7
c = 3
summa = a + b + c
print("Сумма:", summa)
print("Произведение:", a * b * c)
print("Среднее арифметическое:", summa / 3)

print("Меняем значение переменной (вариант 1):")
print("a: " + str(a))
print("b: " + str(b))
a, b = b, a
print("a1: " + str(a))
print("b1: " + str(b))

print("Меняем значение переменной (вариант 2):")
print("a: " + str(a))
print("b: " + str(b))
a = a + b  # a= 5 + 7 = 12
b = a - b  # b = 12 - 7 = 5
a = a - b  # a = 12 - 5 = 7
print("a2: " + str(a))
print("b2: " + str(b))
