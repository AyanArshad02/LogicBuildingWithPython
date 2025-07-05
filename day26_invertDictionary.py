def swap_dict(original_dict):
    swapped = {}

    for key, value in original_dict.items():
        if value not in swapped:
            swapped[value] = [key]
        else:
            swapped[value].append(key)

    return swapped


input_dict = {'a': 1, 'b': 2, 'c': 1}
result = swap_dict(input_dict)
print(result)  
# Output: {1: ['a', 'c'], 2: ['b']}