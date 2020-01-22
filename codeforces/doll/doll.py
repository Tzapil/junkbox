def turn(direction):
    if direction[1] == 1:
        return (1, 0)
    
    if direction[0] == 1:
        return (0, -1)

    if direction[1] == -1:
        return (-1, 0)

    if direction[0] == -1:
        return (0, 1)

n, m, k = [int(x) for x in input().split()]

obst = []
for i in range(k):
    obst.append(tuple(int(x) for x in input().split()))

direction = (0, 1)
pos = (1, 1)

while True:
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if next_pos[0] < 1 or next_pos[0] > n or next_pos[1] < 1 or next_pos[1] > m or next_pos in obst:
        direction = turn(direction)
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos[0] < 1 or next_pos[0] > n or next_pos[1] < 1 or next_pos[1] > m or next_pos in obst:
            if len(obst) == n * m - 1:
                print('Yes')
            else:
                print('No')
            break

    obst.append(tuple(pos))
    pos = next_pos