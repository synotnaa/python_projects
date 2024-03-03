a = []
lst_length= int(input("Введите элементы списка: "))
for i in range(lst_length):
    a.append(int(input("->")))
print("Введённый список: ", a)
print("Введите индекс: ")
index = int(input('k = '))
a.remove(a[index])
print("Обновлённый список: ", a)