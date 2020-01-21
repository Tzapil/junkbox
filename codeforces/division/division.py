# http://codeforces.com/problemset/problem/1203/C

n = int(input())
a = [int(x) for x in input().split(' ')]

a.sort()

def divisiors(num):
    res = {1}
    for i in range(2, num + 1):
        if num % i == 0:
            res.add(i)
    return res

def func():
    res = divisiors(a[0])
    for j in range(1, n):
        res = {x for x in res if a[j] % x == 0}
        if len(res) == 0 or (len(res) == 1 and 1 in res):
            print(len(res))
            return
    print(len(res))
func()