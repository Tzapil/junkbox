def fib(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a + b

print([x for x in fib(100)])
print((x for x in fib(100)))