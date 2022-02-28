t = int(input())

for _ in range(t):
    n = int(input())
    a_ = input()
    a = [int(x) for x in a_.split(' ')]
    q = int(input())
    requests = []
    for _ in range(q):
        requests.append([int(x) for x in input().split(' ')])

    pocket = {}
    for num in a:
        pocket[num] = pocket.get(num, 0) + 1

    has_changed = True
    sorted_requests = sorted([x for x in enumerate(requests)], key=lambda x:x[1][1])

    current_iter = 0
    for step in sorted_requests:
        x, request = step
        indx, iter = request
        if iter > current_iter:
            for _ in range(iter - current_iter):
                if has_changed:
                    has_changed = False
                    new_pocket = {}
                    for i, num in enumerate(a):
                        count = pocket[num]
                        if num != count:
                            has_changed = True
                        a[i] = count
                        new_pocket[count] = new_pocket.get(count, 0) + 1
                    pocket = new_pocket
                else:
                    break
            current_iter = iter
        requests[x] = a[indx - 1]
    
    for x in requests:
        print(x)