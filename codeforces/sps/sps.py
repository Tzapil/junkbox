import math

t = int(input())

rules = {
    'S': 0,
    'P': 2,
    'R': 1
}
for_answer = 'RPS'

for i in range(t):
    n = int(input())
    # R P S
    # a, b, c
    nums = [int(x) for x in input().split(' ')]

    bob = input()

    answer = []
    win = 'YES'
    count = 0

    for choise in bob:
        result = rules[choise]
        if nums[result] > 0:
            count += 1
            answer.append(for_answer[result])
        else:
            answer.append('$')
        nums[result] -= 1

    if count < math.ceil(n/2):
        win = 'NO'
    else:
        for j, a in enumerate(answer):
            if a == '$':
                for i in range(3):
                    if nums[i] > 0:
                        nums[i] -= 1
                        answer[j] = for_answer[i]
                        break
                if answer[j] == '$':
                    win = 'NO'
                    break
    
    print(win)
    if win == 'YES':
        print(''.join(answer))
