coin = input('Введите число от 1 до 99: ')
while type(coin) != int:
    try:
        coin = int(coin)
        last_digit = coin % 10
        if 5 <= last_digit <= 9 or 11 <= coin <= 14:
            print(coin, 'копеек')
        elif last_digit == 1:
            print(coin, 'копейка')
        elif 2 <= last_digit <= 4:
            print(coin, 'копейки')
        else:
            print("Введено некорректное значение")
    except ValueError:
        print('Вы ввели не числовое значение!')
        coin = input('Введите число от 1 до 99: ')
