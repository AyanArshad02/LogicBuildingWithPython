def find_max_keys(dictionary):
    if not dictionary:
        return []

    max_val = max(dictionary.values())
    result = []

    for key, value in dictionary.items():
        if value == max_val:
            result.append(key)

    return result


data = {'a': 10, 'b': 20, 'c': 20}
print(find_max_keys(data))
# Output: ['b', 'c']

print(find_max_keys({'x': 5, 'y': 2, 'z': 5}))
# Output: ['x', 'z']

print(find_max_keys({}))
# Output: []



