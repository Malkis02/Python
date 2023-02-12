array = []
for _ in range(int(input('Введите количество элементов в массиве N = '))):
    array.append(int(input('Введите элемент массива ')))
x = int(input('Введите число X = '))
n = array.count(x)
if 2 <= n % 10 <= 4:
    print(f'Искомое число X встречается в массиве {n} раза.')
else:
   print(f'Искомое число X встречается в массиве {n} раз.') 