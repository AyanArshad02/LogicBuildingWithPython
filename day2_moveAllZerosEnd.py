def move_zeros_to_end(lst):
    count = 0

    for num in lst:
        if num != 0:
            lst[count] = num
            count += 1

    while count < len(lst):
        lst[count] = 0
        count += 1

    return lst


print(move_zeros_to_end([0, 1, 0, 3, 12]))      
print(move_zeros_to_end([0, 0, 0, 5, 1]))       
print(move_zeros_to_end([1, 2, 3]))             
print(move_zeros_to_end([0, 0, 0]))             


