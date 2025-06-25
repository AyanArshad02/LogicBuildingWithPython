def group_words_by_first_letter(words):
    grouped = {}

    for word in words:
        key = word[0]
        if key not in grouped:
            grouped[key] = [word]
        else:
            grouped[key].append(word)

    return grouped


words = ['apple', 'ant', 'banana', 'ball']
result = group_words_by_first_letter(words)
print(result)
# Output: {'a': ['apple', 'ant'], 'b': ['banana', 'ball']}
