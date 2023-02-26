char = 'аеуояиюыэё'

a = len(set([i.count(j) for i in input().split() for j in char if j in i]))
if a == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
