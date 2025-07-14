def compress_string(input_string):
    if not input_string:
        return ""

    compressed = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed += input_string[i - 1] + str(count)
            count = 1

    compressed += input_string[-1] + str(count)

    return compressed

print(compress_string("aaabbc"))   # Output: "a3b2c1"
print(compress_string("abc"))      # Output: "a1b1c1"
print(compress_string("a"))        # Output: "a1"
print(compress_string(""))         # Output: ""


