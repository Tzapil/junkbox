def compact_dict(tree_dict):
    result = []
    stack = [(tree_dict, '')]

    while len(stack) > 0:
        node, path = stack.pop()

        for key in node:
            value = node[key]
            full_path = ((path + '.') if path else '') + key
            if isinstance(value, dict):
                stack.append((value, full_path))
            else:
                result.append((full_path, value))

    return result

a = {
   'b' : 4,
   'c' : {
       'd': 3,
       'e': 5,
    }
}

print(compact_dict(a))