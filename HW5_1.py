def exponentiation(a, b):
    if b == 0:
        return 1
    return exponentiation(a, b - 1) * a

print(exponentiation(int(input()), int(input())))