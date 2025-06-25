def is_palindrome(input_string):
    left = 0
    right = len(input_string) - 1

    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))   # Output: True
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello"))   # Output: False


