n, m = [int(x) for x in input().split(' ')]
c = [int(x) for x in input().split(' ')]
t = input().split(' ')

fo = -1
r = []
for i in range(n + m):
    if t[i] == '1':
        if fo == -1:
            r.append(i)
        else:
            r.append(0)
            for j in range(fo + 1, i):
                df = c[j] - c[fo]
                dl = c[i] - c[j]
                if df <= dl:
                    r[len(r) - 2] += 1
                else:
                    r[len(r) - 1] += 1
        fo = i

r[len(r) - 1] += len(c) - 1 - fo

print(' '.join([str(x) for x in r]))