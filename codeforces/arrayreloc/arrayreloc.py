# 1007A. Перестановка массива

n = int(input())
arr = [(int(x), i) for i, x in enumerate(input().split())]

sort = sorted(arr, key=lambda v: v[0])

# for 

print(sorted(arr, key=lambda v: v[0]))