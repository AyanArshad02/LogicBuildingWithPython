def is_pangram(input_string):
    input_string = input_string.lower()
    seen_letters = set()

    for char in input_string:
        if char.isalpha():
            seen_letters.add(char)

    return len(seen_letters) == 26

print(is_pangram("the quick brown fox jumps over a lazy dog"))  # True
print(is_pangram("hello world"))  # False


