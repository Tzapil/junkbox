import math

q = int(input())

for i in range(q):
    k, n, a, b = [int(x) for x in input().split()]
    
    if b*n >= k:
        print(-1)
    elif a*n < k:
        print(n)
    else:
        x = (k - b*n) / (a - b);

        print(math.ceil(x) - 1)