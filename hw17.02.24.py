print("Найдите все буквы, присутствующие хотя бы в одной строке")
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
b = list(set(str1) | set(str2))
print("Искомыми буквами являются: ")
for i in b:
    print(i, end=" ")