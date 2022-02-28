# 10 10 5 20 = 5
# 2 2 0 4 = -1
# 2 2 2 1 = -1
# 1 5 2 10 = -1
A, B, C, N = [int(x) for x in input().split()]

if N < C or N < A or N < B or C > A or C > B:
    print(-1)
else:
    answer = N - A - B + C

    print(answer if answer >= 1 else -1)

