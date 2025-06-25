def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


print(word_frequency("the cat and the hat"))
# Output: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

print(word_frequency("hello world hello"))
# Output: {'hello': 2, 'world': 1}