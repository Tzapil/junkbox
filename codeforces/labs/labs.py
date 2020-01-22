n = int(input())

a = [[] for _ in range(n)]
for i in range(n):
    direction = i % 2 == 0
    for j in range(1, n + 1):
        if direction:
            a[j - 1].append(str(n * i + j))
        else:
            a[n - j].append(str(n * i + j))

for group in a:
    print(' '.join(group))