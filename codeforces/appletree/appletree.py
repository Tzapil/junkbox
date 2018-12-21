n = int(input())
trees_l = []
trees_r = []

for i in range(n):
    x, a = (int(x) for x in input().split())
    if (x < 0):
        trees_l.append((x, a))
    else:
        trees_r.append((x, a))

count = min(len(trees_l), len(trees_r)) + 1

trees_l = sorted(trees_l, reverse=True)
trees_r = sorted(trees_r)

result = 0

for i in range(min(count, len(trees_l))):
    result += trees_l[i][1]
for i in range(min(count, len(trees_r))):
    result += trees_r[i][1]

print(result)