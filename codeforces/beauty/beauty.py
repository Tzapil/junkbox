import re

n = int(input())
result = []

vowels = re.compile(r'[aeoiu]')
vowel = set("aeiou") 

def count_vowels(string):
    count = 0
    last = ''
    for alphabet in string:
        if alphabet in vowel: 
            count += 1
            last = alphabet
    return (count, last)

if n >=4:
    words = {}
    second_parts = []
    first_parts = []

    for i in range(n):
        word = input()
        vows, last = count_vowels(word)
        if vows not in words:
            words[vows] = {
                'array': []
            }

        hm = words[vows]
        if last not in hm:
            hm[last] = [word]
            words[vows]['array'].append(word)
        else:
            get = False
            for v in hm[last]:
                if v != word:
                    second_parts.append((v, word))
                    hm[last].remove(v)
                    words[vows]['array'].remove(v)
                    get = True
                    break
            if not get:
                hm[last].append(word)
                words[vows]['array'].append(word)
    
    for l in words:
        arr = words[l]['array']
        while len(arr) >= 2:
            fp = arr.pop()
            sp = arr.pop()
            first_parts.append((fp, sp))

    while len(second_parts) >= 1 and (len(second_parts) + len(first_parts)) > 1:
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