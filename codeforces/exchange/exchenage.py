with open('input.txt', 'r') as fr:
    result = int(fr.readline())
    for i in range(3):
        a,b = [int(x) for x in fr.readline().split()]
        if a == result:
            result = b
        elif b == result:
            result = a

with open('output.txt', 'w') as fw:
    fw.write(str(result))