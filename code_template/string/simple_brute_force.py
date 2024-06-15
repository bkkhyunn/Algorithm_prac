# 배열 탐색
def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 문자열 비교
def str_compare(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

    small_length = min(length_s1, length_s2)

    for i in range(small_length):
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])

    if (length_s1 == length_s2):
        return 0
    elif length_s1 > length_s2:
        return s1[small_length]
    else:
        return s2[small_length]