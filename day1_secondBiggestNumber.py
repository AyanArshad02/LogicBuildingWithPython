def find_second_largest(lst):
    if len(lst) < 2:
        return -1  # Not enough elements

    max_val = float('-inf')

    # First pass – Find the maximum value
    for num in lst:
        if num > max_val:
            max_val = num

    second_max = -1

    # Second pass – Find the largest value less than max_val
    for num in lst:
        if num != max_val and num > second_max:
            second_max = num

    return second_max


print(find_second_largest([12, 35, 1, 10, 34, 1]))   # Output: 34
print(find_second_largest([10, 5, 10]))              # Output: 5
print(find_second_largest([10, 10, 10]))             # Output: -1