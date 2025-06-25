def move_zeros_to_end(lst):
    count = 0  # Position to place the next non-zero element

    # First pass – move all non-zero elements to the front
    for num in lst:
        if num != 0:
            lst[count] = num
            count += 1

    # Second pass – fill the rest of the list with zeros
    while count < len(lst):
        lst[count] = 0
        count += 1

    return lst


print(move_zeros_to_end([0, 1, 0, 3, 12]))      # Output: [1, 3, 12, 0, 0]
print(move_zeros_to_end([0, 0, 0, 5, 1]))       # Output: [5, 1, 0, 0, 0]
print(move_zeros_to_end([1, 2, 3]))             # Output: [1, 2, 3]
print(move_zeros_to_end([0, 0, 0]))             # Output: [0, 0, 0]


