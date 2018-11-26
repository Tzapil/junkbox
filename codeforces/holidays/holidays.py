n = int(input())

max, min = 0, 0
if n == 1:
    answer = (0, 1)
elif n <= 5:
    answer = (0, 2)
if n % 7 == 0:
    max = min = n / 7 * 2
elif (n + 1) % 7 == 0:
    max = (n + 1) / 7 * 2
    min = max - 1
elif (n + 2) % 7 == 0:
    max = (n + 2) / 7 * 2
    min = max - 2
elif (n - 1) % 7 == 0:
    min = (n - 1) / 7 * 2
    max = min + 1
else:
    min = int(n / 7) * 2
    max = min + 2

print(int(min), int(max))