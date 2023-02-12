n = int(input("Введите количество монеток: "))
countA = 0
countB = 0
for i in range(n):
    temp = int(input(f"Введите {i + 1} монетку: "))
    if temp == 0:
        countA += 1
    elif temp == 1:
        countB += 1
print(min(countA, countB))