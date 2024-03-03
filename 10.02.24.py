# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def set_param(c=20, s="-"):
#     print(c * s, end='')
#     print()
#
#
# set_param()
# set_param(7)
# set_param(15, '*')
# set_param(s='#')

#########################################################
# def digits_sum(n):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if cur_digit % 2 == 0:
#             s += cur_digit
#         n //= 10
#         if not even and cur_digit % 2:
#             s+= cur_digit
#     return s
#
#
# print("Сумма чётных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))

#########################################################

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")

#########################################################

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2) # с помощью оператора is можно проверить ссылается ли элемент на один и тот же id в памяти
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
#
# a = a + "_new"
# print(a)

# lt1 = [1, 20, 3]
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))

# неизменяемые типы данных (на сегодяншний день) - int, str, float, bool
# изменяемые типы данных - list

#########################################################

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# print(tpl[1])
# print(type(tpl))

a = ()
print(a, type(a))

# b = tuple("Hello")

print(b, type(b))

