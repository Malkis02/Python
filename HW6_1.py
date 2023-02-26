a = int(input())
d = int(input())
n = int(input())

a_n = []
for i in range(n):
    a_n.append(a + i * d)
print(a_n)