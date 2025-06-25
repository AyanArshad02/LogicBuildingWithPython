def reverse_each_word(sentence):
    # Step 1: Split the sentence into words
    words = sentence.split()

    # Step 2: Create a new list to store reversed words
    reversed_words = []

    # Step 3: Reverse each word and add to the list
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    # Step 4: Join the reversed words into a sentence
    result = ' '.join(reversed_words)

    return result

print(reverse_each_word("data science"))
# Output: "atad ecneics"

print(reverse_each_word("hello world"))
# Output: "olleh dlrow"



