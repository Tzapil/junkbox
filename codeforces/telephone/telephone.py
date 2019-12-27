n = int(input())
s = input()

count = 0
last = -1
steps = n - 11
petya = int(steps/2)
vaysa = steps - petya
found = False
for indx, symbol in enumerate(s):
    if symbol == '8':
        t = vaysa - indx + count
        if t >= 0:
            if petya <= count:
                found = True
                break
        else:
            break
        count += 1
if not found:
    print('NO')
else:
    print('YES')
