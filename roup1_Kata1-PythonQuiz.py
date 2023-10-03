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

def solution(S):
    words = S.split()

    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    result = " ".join(reversed_words)

    return result

S = "how are you Faith?"
result = solution(S)
print(result)

