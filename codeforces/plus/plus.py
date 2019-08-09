h, w = [int(x) for x in input().split()]

def check_row(row):
    first_star = row.find('*')
    last_star = row.rfind('*')
    stars = row[first_star:last_star + 1]
    return stars.find('.') == -1 and len(stars) > 1

def check():
    matrix = []
    r = -1
    c = -1
    for i in range(h):
        row = input()
        count = row.count('*')
        if count > 0:
            index = row.find('*')
            if count == 1:
                if c == -1:
                    c = index
                elif c != index:
                    return False
            else:
                if r != -1:
                    return False
                else:
                    r = i
                    if not check_row(row):
                        return False
        matrix.append(row)

    if r == 0 or r == (h -1 ) or c == 0 or c == (w - 1):
        return False
    else:
        steps = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        for s1, s2 in steps:
            if matrix[r + s1][c + s2] != '*':
                return False

        row = ''.join([x[c] for x in matrix])
        if not check_row(row):
            return False
        

    return True

    

print('YES' if check() else 'NO')