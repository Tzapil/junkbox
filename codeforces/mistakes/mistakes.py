string = input()

count = 0
last = ''
result = []
last_count = 0

for char in string:
    if char == last:
        count += 1
    else:
        if count >= 2:
            repeat = 2

            if last_count >= 2 and count >= 2:
                repeat = 1
                count = 1
            result.append(last * repeat)
        else:
            result.append(last)

        last = char
        last_count = count
        count = 1

if count >= 2:
    repeat = 2

    if last_count >= 2 and count >= 2:
        repeat = 1
    result.append(last * repeat)
else:
    result.append(last)

print(''.join(result))