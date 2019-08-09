t = int(input())

for _ in range(t):
    x = input()
    y = input()

    z_x = int(x, 2)
    z_y = int(y, 2)

    k = 0
    minimum = -1
    result = 0
    maximum = len(x)

    while k < maximum:
        temp = "{0:b}".format(z_x + z_y)[::-1]
        if minimum == -1 or temp < minimum:
            result = k
            minimum = temp

        k += 1
        z_y = z_y << 1

    print(result)