import math

n = int(input())

x = math.ceil(n / 2) - 1

if x % 2 == 0 and n % 2 == 0:
    x -= 1

print(x, n - x)