n = int(input())
s1 = input()
s2 = input()

def get_result(s1, s2):
    result = []
    diffAB = set()
    diffBA = set()

    for i in range(0, n):
        if s1[i] != s2[i]:
            if s1[i] == 'b':
                diffBA.add(i)
            else:
                diffAB.add(i)

    count = len(diffAB) + len(diffBA)
    if count == 0:
        return 0
    if count % 2 != 0:
        return -1

    while len(diffBA) >= 2:
        a = diffBA.pop()
        b = diffBA.pop()

        result.append((a, b))

    while len(diffAB) >= 2:
        a = diffAB.pop()
        b = diffAB.pop()

        result.append((a, b))

    if len(diffAB) != 0:
        ab = diffAB.pop()
        ba = diffBA.pop()
        result.append((ab, ab))
        result.append((ab, ba))

    return result

r = get_result(s1, s2)

if not isinstance(r, list):
    print(r)
else:
    print(len(r))
    for a, b in r:
        print(a + 1, b + 1)




