def split_into_chunks(lst, k):
    chunks = []
    for i in range(0, len(lst), k):
        chunks.append(lst[i:i+k])
    return chunks

print(split_into_chunks([1, 2, 3, 4, 5, 6, 7], 3))
# Output: [[1, 2, 3], [4, 5, 6], [7]]

print(split_into_chunks([10, 20, 30, 40, 50], 2))
# Output: [[10, 20], [30, 40], [50]]