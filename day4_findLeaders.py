def find_leaders(lst):
    leaders = []

    for i in range(len(lst)):
        is_leader = True

        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                is_leader = False
                break

        if is_leader:
            leaders.append(lst[i])

    return leaders


print(find_leaders([16, 17, 4, 3, 5, 2]))   # Output: [17, 5, 2]
print(find_leaders([1, 2, 3, 4, 0]))        # Output: [4, 0]
print(find_leaders([7, 10, 4, 10, 6, 5, 2]))# Output: [10, 10, 6, 5, 2]