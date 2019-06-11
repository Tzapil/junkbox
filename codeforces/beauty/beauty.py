import re

n = int(input())
result = []

vowels = re.compile(r'[aeoiu]')

def count_vowels(string):
    vows = re.findall(vowels, string)
    return (len(vows), vows[-1])

def pop_2(arr):
    fp = arr.pop()
    sp = arr.pop()

    return (fp, sp)

if n >=4:
    words = {}
    for i in range(n):
        word = input()
        vows, last = count_vowels(word)
        if vows not in words:
            words[vows] = {
                'array': []
            }

        hm = words[vows]
        if last not in hm:
            hm[last] = []

        words[vows]['array'].append(word)
        hm[last].append(word)
    
    second_parts = []
    first_parts = []
    for l in words:
        for v in words[l]:
            arr = words[l][v]
            if v == 'array':
                continue

            while len(arr) >= 2:
                fp, sp = pop_2(arr)
                second_parts.append((fp, sp))

                words[l]['array'].remove(fp)
                words[l]['array'].remove(sp)
        
        arr = words[l]['array']
        while len(arr) >= 2:
            fp, sp = pop_2(arr)
            first_parts.append((fp, sp))

    while (len(second_parts) + len(first_parts)) >= 1:
        fp = None
        if len(first_parts) == 0:
            fp = second_parts.pop()
        else:
            fp = first_parts.pop()
            
        sp = second_parts.pop()

        result.append('{0} {1}\n{2} {3}'.format(fp[0], sp[0], fp[1], sp[1]))

print(len(result))
if (len(result) > 0):
    print('\n'.join(result))