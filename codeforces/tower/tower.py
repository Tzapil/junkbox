n = int(input())

a = [int(x) for x in input().split(' ')]

isLower = False
last = -1

valid = True

for i in a:
    if not isLower:
        if i < last:
            isLower = True
    else:
        if i > last:
            valid = False
            break
    
    last = i

print('YES' if valid else 'NO')
        