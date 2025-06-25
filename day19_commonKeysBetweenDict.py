def find_common_keys(dict1, dict2):
    common_keys = []

    for key in dict1:
        if key in dict2:
            common_keys.append(key)

    return common_keys


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print(find_common_keys(dict1, dict2))  # Output: ['b']


