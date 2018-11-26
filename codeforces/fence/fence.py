n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

last = 0
for i in range(k):
    last += h[i]

answer = last
index = 0

for i in range(k, n):
    next = last + h[i] - h[i - k]
    if next < answer:
        answer = next
        index = i - k + 1
    last = next

print(index + 1)