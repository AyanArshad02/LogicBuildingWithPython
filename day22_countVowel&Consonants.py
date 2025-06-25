def count_vowels_and_consonants(input_string):
    vowel_count = 0
    consonant_count = 0

    vowels = {'a', 'e', 'i', 'o', 'u'}

    for char in input_string:
        char = char.lower()

        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

string = "hello"
vowels, consonants = count_vowels_and_consonants(string)
print("Vowels:", vowels)
print("Consonants:", consonants)
# Output: Vowels: 2, Consonants: 3



