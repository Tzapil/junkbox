q = int(input())

for i in range(q):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if n == 1:
        print(a[0])
    else:
        a.sort()
        if a[-1] - a[0] > 2*k:
            print(-1)
        else:
            print(a[0] + k)