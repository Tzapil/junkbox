n = int(input())
pages = [int(x) for x in input().split()]

i = 0
while n > 0:
    i = 1 + i % 7
    n -= pages[i - 1]

print(i)