def merge_dictionaries(dict1, dict2):
    merged = {}

    # Add all items from dict1
    for key, value in dict1.items():
        merged[key] = value

    # Add items from dict2, summing if key already exists
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value

    return merged


dict1 = {'a': 5, 'b': 3}
dict2 = {'a': 2, 'c': 4}

result = merge_dictionaries(dict1, dict2)
print(result)
# Output: {'a': 7, 'b': 3, 'c': 4}


