def sort_dict_by_value_desc(dictionary):

    items = list(dictionary.items())  # [('a', 3), ('b', 1), ('c', 5)]

    # Step 2: Sort the items using the value (index 1 of each tuple)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:  # Compare values
                # Swap if the value at i is less than value at j
                items[i], items[j] = items[j], items[i]

    # Step 3: Return the sorted list of tuples
    return items


data = {'a': 3, 'b': 1, 'c': 5}
print(sort_dict_by_value_desc(data))
# Output: [('c', 5), ('a', 3), ('b', 1)]


