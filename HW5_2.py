def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print(sum(int(input()), int(input())))