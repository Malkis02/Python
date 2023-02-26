def print_operation_table(operation, rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            operation(i, j)
            print(i * j, end=" \a")
        print("\n")


print_operation_table(lambda x, y: x * y, int(input()), int(input()))
