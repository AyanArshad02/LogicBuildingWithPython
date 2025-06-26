def contains_duplicate(lst):
    freq = {}

    for num in lst:
        if num in freq:
            return True
        else:
            freq[num] = 1

    return False


print(contains_duplicate([1, 2, 3, 4, 1]))   # Output: True
print(contains_duplicate([1, 2, 3, 4, 5]))   # Output: False
print(contains_duplicate([]))               # Output: False
print(contains_duplicate([7, 7]))           # Output: True


