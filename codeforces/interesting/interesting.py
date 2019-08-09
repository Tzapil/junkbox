inpt = input()
n = [int(x) for x in list(inpt)]
num = int(inpt)

while True:
    sum = 0
    for i in n:
        sum += i
    mod = sum % 4
    if mod == 0:
        break
    num += (4 - mod)
    n = [int(x) for x in list(str(num))]

print(num)