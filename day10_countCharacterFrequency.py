def count_char_frequency(input_string):
    freq = {}

    for char in input_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

print(count_char_frequency("data"))
# Output: {'d': 1, 'a': 2, 't': 1}

print(count_char_frequency("mississippi"))
# Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}