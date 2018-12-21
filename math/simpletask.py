def findK(s, k=1):
    if len(s) == 0:
        return 0

    answer = 1
    letters = [s[0]]
    length = [0]
    for i in range(len(s)):
        if s[i] in letters:
            length[-1] += 1
        else:
            if len(letters) >= k:
                count = sum(length)
                if count > answer:
                    answer = count
                letters.pop(0)
                length.pop(0)
            letters.append(s[i])
            length.append(1)
            

    count = sum(length)
    if count > answer:
        answer = count

    return answer

print(findK(''))
print(findK('a'))
print(findK('abbc'))
print(findK('abbccccccc'))
print(findK('adddaabaa'))
