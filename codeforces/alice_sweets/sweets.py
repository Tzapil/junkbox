q = int(input())

for _ in range(q):
    s = [int(x) for x in input().split(' ')]
    s.sort()
    b = s[2]
    a = s[1] + s[0]

    a += (b - a) // 2

    print(a)