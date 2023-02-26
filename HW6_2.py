list_1 = list(map(int, input().split()))
num_min = int(input())
num_max = int(input())

print([i for i in range(len(list_1)) if num_min <= list_1[i] <= num_max])
