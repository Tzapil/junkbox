n = int(input())
c = [int(x) for x in input().split(' ')]
d = 1
count = 0
turns = 0

while count < n:
    rng = range(len(c))
    if d == -1:
        rng = range(len(c) - 1, -1, -1)
    for indx in rng:
        item = c[indx]
        if item != -1 and item <= count:
            count += 1
            c[indx] = -1
    d = d * -1
    if count < n:
        turns += 1

print(turns)