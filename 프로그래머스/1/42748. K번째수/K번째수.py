def solution(array, commands):
    answer = []
    for i, j, k in commands:
        array_ = array[i-1:j]
        array_.sort()
        answer.append(array_[k-1])
    return answer