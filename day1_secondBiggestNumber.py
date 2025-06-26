def find_second_largest(lst):
    if len(lst) < 2:
        return -1

    max_val = float('-inf')

    for num in lst:
        if num > max_val:
            max_val = num

    second_max = -1

    for num in lst:
        if num != max_val and num > second_max:
            second_max = num

    return second_max


print(find_second_largest([12, 35, 1, 10, 34, 1]))
print(find_second_largest([10, 5, 10]))
print(find_second_largest([10, 10, 10]))