n, m = [int(x) for x in input().split(' ')]
a = [int(x) for x in input().split(' ')]

a.sort()

r = []

step = 1
current = 0
while m > 0 and m >= step:
    if current < n and a[current] == step:
        current += 1
        step += 1
        continue

    m -= step
    r.append(str(step))
    step += 1

print(len(r))
print(' '.join(r))
