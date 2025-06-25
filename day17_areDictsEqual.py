def are_dicts_equal(dict1, dict2):
    # Step 1: Check if lengths are equal
    if len(dict1) != len(dict2):
        return False

    # Step 2: Compare keys and values
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False

    # Step 3: All checks passed
    return True



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(are_dicts_equal(dict1, dict2))  # Output: True

dict3 = {'a': 1, 'b': 3}
print(are_dicts_equal(dict1, dict3))  # Output: False
