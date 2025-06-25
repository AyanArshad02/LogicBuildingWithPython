def extract_nested_values(data, target_key):
    result = []

    for inner_dict in data.values():
        if target_key in inner_dict:
            result.append(inner_dict[target_key])

    return result



data = {
    'emp1': {'name': 'Alice', 'age': 30},
    'emp2': {'name': 'Bob', 'age': 25}
}

print(extract_nested_values(data, 'name'))
# Output: ['Alice', 'Bob']

print(extract_nested_values(data, 'age'))
# Output: [30, 25]

print(extract_nested_values(data, 'department'))
# Output: []
