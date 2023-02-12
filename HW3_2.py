array = []
min_distance = 1000000
for _ in range(int(input('Введите количество элементов в массиве N = '))):
    array.append(int(input('Введите элемент массива ')))
x = int(input('Введите число X = '))
for i in range(len(array)):
    distance = abs(x - array[i])
    if distance < min_distance:
        min_distance = distance
        nearest = array[i]
print(f'Самый близкий по величине элемент к заданному числу {x} равен {nearest}.')