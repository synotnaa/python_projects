import math

print('Вычисление площади фигур')
print('Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг')
fig = int(input('Выберите фигуру:'))
if fig == 1:  # s = sqrt(0.5*(a+b+c)*(0.5*(a+b+c)-a)*(0.5*(a+b+c)-b)*(0.5*(a+b+c)-c))
    a = int(input('Введите сторону a:'))
    b = int(input('Введите сторону b:'))
    c = int(input('Введите сторону c:'))
    s = math.sqrt(0.5 * (a + b + c) * (0.5 * (a + b + c) - a) * (0.5 * (a + b + c) - b) * (0.5 * (a + b + c) - c))
    print(round(s, 2))
if fig == 2:
    a = int(input('Введите сторону a:'))
    b = int(input('Введите сторону b:'))
    s = a * b
    print(round(s, 2))
if fig == 3:
    r = int(input('Введите радиус r:'))
    s = math.pi * r ** 2
    print(round(s, 2))