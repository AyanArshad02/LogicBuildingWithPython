def is_anagram(str1, str2):
    # Step 1: Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Step 2: Create dictionaries to count characters
    count1 = {}
    count2 = {}

    # Step 3: Count characters in str1
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    # Step 4: Count characters in str2
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    # Step 5: Compare both dictionaries
    return count1 == count2


print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
print(is_anagram("evil", "vile"))      # Output: True



