s1 = input()
s2 = input()

i = 1
j = 1

while s1[-i] == s2[-j]:
    i += 1
    j += 1

    if i > len(s1) or j > len(s2):
        break


i -= 1
j -= 1

print(len(s1) - i + len(s2) - j)