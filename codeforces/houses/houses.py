n = int(input())
houses = [int(x) for x in input().split(' ')]

i = 0
j = n - 1
maximum = 0

if houses[i] == houses[j]:
    while houses[i] == houses[0] and j > i:
        i += 1
    while houses[j] == houses[0] and j > i:
        j -= 1
    maximum = i
    if (n - j - 1) < maximum:
        maximum = n - j - 1

print(n - 1 - maximum)