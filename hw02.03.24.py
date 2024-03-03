print('Вариант 1')


def outer(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))

# var2
print('Вариант 2. Глобальная переменная')


def outer(a, b, c):
    global s

    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


outer(2, 4, 6)
print(s)
outer(5, 8, 2)
print(s)
outer(1, 6, 8)
print(s)

# ------------------------------------------------------------------------------

print('Вариант 3. Нелокальная переменная')


def outer(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s

print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))

