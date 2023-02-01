num = int(input("Введите число \n"))
result = 0
while num > 0:
    last = num % 10
    result += last
    num //= 10
print(result)
