import os

keys = []

for (dirpath, dirnames, filenames) in os.walk("./keys"):
    for file in filenames:
        with open(f'./keys/{file}', 'r') as fp:
            keys.append(fp.read())

keys.sort()

print('\n'.join(keys))