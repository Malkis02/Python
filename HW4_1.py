n = int(input('Введите количество элементов первого множества '))
m = int(input('Введите количество элементов второго множества '))
array_1 = []
array_2 = []

array_1 = [int(input('Введите элемент первого множества ')) for _ in range(n)]
array_2 = [int(input('Введите элемент второго множества ')) for _ in range(m)]
array_1.extend(array_2)
array = list(set(array_1))

result = []
for i in range(len(array)):
    result.append(min(array))
    array.remove(min(array))
print('Полученный набор чисел:', *result)