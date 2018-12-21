def intervals(arr):
    result = []
    current = []
    last = None
    for i in sorted(arr):
        if i - 1 == last:
            current = (current[0], i)
        else:
            if len(current):
                result.append(current)
            current = (i, )
        last = i

    if len(current):
        result.append(current)
    return result

def intervals_str(arr):
    if len(arr) == 0:
        return []

    result = []
    begin = 0
    sort_arr = sorted(arr)
    for i in range(len(arr) - 1):
        if sort_arr[i] + 1 != sort_arr[i + 1]:
            interval = str(sort_arr[begin])
            if begin != i:
                interval += "-" + str(sort_arr[i])
            result.append(interval)
            begin = i + 1
        
    interval = str(sort_arr[begin])
    if begin != len(arr) - 1:
        interval += "-" + str(sort_arr[-1])
    result.append(interval)

    return result

print(", ".join([str(x) for x in intervals_str([1, 4, 5, 2, 3, 9, 8, 11, 0])]))