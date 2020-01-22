import math

n, m = [int(x) for x in input().split()]

print(int(pow(pow(2, m, 1000000007) - 1, n, 1000000007)))
