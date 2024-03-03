num1 = int(input('Введите пятизначное число: '))
if 10000 <= num1 <= 99999:
    num = num1
    a = num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    c = num % 10
    num = num // 10
    d = num % 10
    num = num // 10
    e = num % 10
    num = num // 10
    print('Произведение цифр числа:', num1, a*b*c*d*e)
    print('Среднее арифметическое:', a*b*c*d*e/5)
else:
    print('Вы ввели некорректное число')
