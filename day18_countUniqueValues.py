def count_unique_values(dictionary):
    # Step 1: Get all values
    values = dictionary.values()

    # Step 2: Convert values to a set to get unique values
    unique_values = set(values)

    # Step 3: Return the number of unique values
    return len(unique_values)


data = {'a': 1, 'b': 2, 'c': 1}
print(count_unique_values(data))  # Output: 2

data2 = {'x': 5, 'y': 5, 'z': 5}
print(count_unique_values(data2))  # Output: 1

data3 = {}
print(count_unique_values(data3))  # Output: 0


