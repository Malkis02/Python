n = int(input('Введите количество кустов N '))
lot_berry = [
    int(input(f'Введите количество ягод на {i} кусте ')) for i in range(1, n + 1)]
max_count_berry = 0
count_berry = 0
for i in range(n):
    if i == 0:
        count_berry = lot_berry[0] + lot_berry[1] + \
            lot_berry[len(lot_berry) - 1]
    elif i == len(lot_berry) - 1:
        count_berry = lot_berry[0] + \
            lot_berry[len(lot_berry) - 2] + lot_berry[len(lot_berry) - 1]
    else:
        count_berry = lot_berry[i - 1] + lot_berry[i] + lot_berry[i + 1]
    if max_count_berry < count_berry:
        max_count_berry = count_berry
        ind = i + 1
print(
    f'Максимальное количество ягод, которое может собрать за один заход собирающий модуль, равно {max_count_berry}.')
print(f'При этом он будет находиться перед кустом {ind}.')