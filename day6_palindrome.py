def is_palindrome(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1

    return True

print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
print(is_palindrome([1, 2, 3, 4, 5]))  # Output: False
print(is_palindrome([]))              # Output: True
print(is_palindrome([1]))             # Output: True


