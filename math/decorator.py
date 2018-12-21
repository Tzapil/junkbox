def recall(func_or_param):
    tries = -1
    func = func_or_param

    def inner(*args, **kwargs):
        called = False
        result = None
        step = 0
        while not called:
            try:
                step += 1
                result = func(*args, **kwargs)
                called = True
            except Exception as e:
                if tries != -1 and step > tries:
                    raise e

        return result

    def wrapper(wr):
        nonlocal func
        func = wr
        return inner

    if not callable(func_or_param):
        tries = func_or_param
        return wrapper

    return inner

a = 0

@recall(5)
def unstable():
    global a
    a = a + 1
    if a < 5:
        raise Exception('BAM')

    return a * a

print(unstable())

def foo(x=[]):
    x.append(1)
    print(x)

foo()
foo([2])
foo()

t = ([1, 2], 'asdf', 4.)
# t[1] = 'qwer'
t[0].append(3)
# t[0] += [4, 5]