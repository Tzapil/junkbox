n = int(input())

result = [1]
step = 2
count = 3

while count <= n:
    result.append(step)
    step += 1
    count += step

result[-1] += (n - count + step)

print(len(result))
print(' '.join([str(x) for x in result]))