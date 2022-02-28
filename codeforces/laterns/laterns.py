n, l = [int(x) for x in input().split(' ')]
a = [int(x) for x in input().split(' ')]
a.append(l)
a.sort()

current = 0
d = 0

for i, a_i in enumerate(a):
    dividor = 2
    if i == 0 or i == len(a) - 1:
        dividor = 1
    dist = (a_i - current) / dividor
    if dist > d:
        d = dist
    
    current = a_i

print('%.9f' % d)