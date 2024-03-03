def set_param(c=5, s="#", q=1):
    if q == 0:  # горизонтальная линия
        print(c * s, end='')
    elif q == 1: #вертикальная линия
        for i in range(c):
            print(s)
    else:
        print('Укажите тип линии (0 - горизонтальная, 1 - вертикальная)')

set_param()
