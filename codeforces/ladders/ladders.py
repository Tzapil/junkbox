t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]

    if n <= 2:
        print(0)
        continue

    max = -1
    smax = -1

    for i in a:
        if i > max:
            smax = max
            max = i
            continue

        if i > smax and i <= max:
            smax = i

    r = min(smax - 1, len(a) - 2)

    print(r)