# 3 7
# 2 1
# 3 8
# 5 2
# == 11

# 5 10
# 2 77
# 3 33
# 8 21
# 9 12
# 10 64
# == 79

n, s = [int(x) for x in input().split()]
a = []

for _ in range(n):
    # этаж, время
    a.append([int(x) for x in input().split()])
    
a.sort(key=lambda x: x[0], reverse=True)

time = 0
for floor, sec in a:
    time += s - floor
    if time < sec:
        time = sec
    s = floor
    
time += s
    
print(time)