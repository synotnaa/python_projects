d = {
    "emp1": {"name": "John", "salary":  7500},
    "emp2": {"name": "Emma", "salary":  8000},
    "emp3": {"name": "Brad", "salary":  6500},
}
# print(d["emp3"])

for x in d:
    print(x)
    for y in d[x]:
        print("\t", y, ":", d[x][y])

person = input("Введите имя: ")
salary = input("Зарплата: ")
print(d[person][salary])

new_data = int(input("Новое значение: "))
d[person][salary] = new_data
print(d[person])