def count():
    a = int(input('введите число: '))
    n = int(input('введите цифру: '))
    c = 0
    for i in range(0, len(str(a))):
        if int(str(a)[i]) == n:
            c += 1
    return c

print(count())
