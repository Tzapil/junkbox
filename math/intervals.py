def intersection(first, second):
    i = 0
    lf = len(first)
    j = 0
    ls = len(second)

    answer = []

    while i < lf and j < ls:
        if first[i][1] <= second[j][0]:
            i += 1
            continue
        if second[j][1] <= first[i][0]:
            j += 1
            continue
        
        answer.append((max(first[i][0], second[j][0]), min(first[i][1], second[j][1])))

        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return answer

print(intersection([(8, 12), (17, 22)], [(5, 11), (14, 20)]))