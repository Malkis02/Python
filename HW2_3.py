# num = int(input("Введите число \n"))
# for i in range(2, num, 2):
#     print(i)
finish = int(input('Введите N = '))
i = 0
while 2**i < finish:
    print(2**i, end=' ')
    i += 1