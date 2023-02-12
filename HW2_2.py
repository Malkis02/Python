total = int(input('Сумма задуманных чисел S равна '))
product = int(input('Произведение задуманных чисел P равно '))
flag = False
for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == total and i * j == product:
            flag = True
            x = i
            y = j
        j += 1
    i += 1
if flag:
    print('Петя задумал числа {} и {}.'.format(x, y))
else:
    print('Увы, Петя ошибся, такие целые числа невозможно подобрать.')