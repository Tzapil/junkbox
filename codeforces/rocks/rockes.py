t = int(input())

for i in range(t):
    a, b, c = [int(x) for x in input().split()]

    step1 = min(c // 2, b)
    max_rocks = 3 * (step1 + min((b - step1) // 2, a))

    print(max_rocks)
