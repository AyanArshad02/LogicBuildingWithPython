def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    result = ' '.join(reversed_words)

    return result

print(reverse_each_word("data science"))
# Output: "atad ecneics"

print(reverse_each_word("hello world"))
# Output: "olleh dlrow"



