n, m = [int(x) for x in input().split()]

a = []

for _ in range(m):
    a.append([int(x) for x in input().split()])
    
s = 0
common_city = set(x + 1 for x in range(n))
for x in a:
    if x[0] in common_city:
        common_city.remove(x[0])
    if x[1] in common_city:
        common_city.remove(x[1])


random_common = common_city.pop()
print(n - 1)
for x in range(n):
    if x + 1 != random_common:
        print(x + 1, random_common)