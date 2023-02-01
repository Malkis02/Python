num = int(input("Введите номер билета \n"))
total1, total2 = 0, 0
if num > 999999 or num < 99999:
    print("Введено не корректное число")
else:
    for i in str(num % 1000):
        total1 += int(i)
    for j in str(num // 1000):
        total2 += int(j)
    print("Счастливый" if total1 == total2 else "Несчастливый")
