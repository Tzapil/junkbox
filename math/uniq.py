from functools import reduce

with open('./a.txt', 'r') as file:
    # with open('./a_out.txt', 'w') as out_file:
    last_line = None
    for line in file:
        if last_line != line:
            print(line)
        last_line = line
            
with open('./a.txt', 'r') as file:
    # with open('./a_out.txt', 'w') as out_file:
    print(reduce(lambda acc, item: acc + [item] if len(acc) == 0 or acc[-1] != item else acc, file.readlines(), []))