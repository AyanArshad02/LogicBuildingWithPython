def count_frequencies(lst):
    freq = {}

    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    return freq


print(count_frequencies([1, 2, 2, 3, 1, 4, 2]))
# Output: {1: 2, 2: 3, 3: 1, 4: 1}

print(count_frequencies(["a", "b", "a", "c", "b", "a"]))
# Output: {'a': 3, 'b': 2, 'c': 1}