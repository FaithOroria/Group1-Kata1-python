def solution (S):
    char_count = {}

    for char in S:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1

    deletions = 0

    for count in char_count.values():
        if count % 2 != 0:
            deletions +=1

    return deletions

S = "acbcbba"
result = solution(S)
print(result)
