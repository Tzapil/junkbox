l = int(input())

crypted_word = list(input())

result = []

for step in reversed(range(l)):
    pos = (l - 1 - step) // 2
    result.insert(pos, crypted_word[step])

print(''.join(result))
