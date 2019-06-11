import math

n, k = [int(x) for x in input().split()]

division = 1
if n < k:
    division = math.floor(k / n)
    reminder = k % n
    if reminder != 0:
        division += 1
    print(reminder)
print(division)