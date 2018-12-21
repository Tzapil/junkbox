def is_binary_search_tree(root):
    if root is None:
        return True

    def recursive(root):
        value = root['value']
        left_check = root['value']
        right_check = root['value']
        if 'left' in root and root['left'] is not None:
            left_check = recursive(root['left'])[1]
            if not bool(left_check) or left_check > value:
                return False

        if 'right' in root and root['right'] is not None:
            right_check = recursive(root['right'])[0]
            if not bool(right_check) or right_check < value:
                return False

        return (left_check, right_check)

    return bool(recursive(root))


root = {
    'value': 4,
    'left': {
        'value': 2,
        'left': {
            'value': 1
        },
        'right': {
            'value': 3
        }
    },
    'right': {
        'value': 5
    }
}

root2 = {
    'value': 3,
    'left': {
        'value': 2,
        'left': {
            'value': 1
        },
        'right': {
            'value': 4
        }
    },
    'right': {
        'value': 5
    }
}

print(is_binary_search_tree(root))
print(is_binary_search_tree(root2))