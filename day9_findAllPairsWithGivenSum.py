def find_pairs(lst, target):
    seen_numbers = set()
    result_pairs = set()

    for num in lst:
        complement = target - num

        if complement in seen_numbers:
            pair = (min(num, complement), max(num, complement))
            result_pairs.add(pair)

        seen_numbers.add(num)

    return list(result_pairs)

lst = [2, 4, 3, 5, 7]
target = 7

print(find_pairs(lst, target))  # Output: [(2, 5), (3, 4)]


