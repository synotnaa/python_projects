import random

w, h = 3, 4
matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
for row in matrix:
    for x in row:
        print(x, end='\t\t')
    print()

print(matrix)
count = 0

for row in matrix:
    for i in row:
        if i < 0:
            count += 1
print(i)