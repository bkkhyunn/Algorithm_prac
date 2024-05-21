def solution(numbers):
    s_numbers = [str(n) for n in numbers]
    # 1000 이하의 원소이기 때문에 3을 곱해주면 '000' 식이 되고
    # 거기서 정렬하면 한자리 수와 같은 수의 두, 세자리 수의 크기를 비교하기 용이하다.
    # 3, 30 에서 3이 크게 되고, 3, 34 에서는 34가 크게 된다.
    s_numbers.sort(key=lambda x: x*3, reverse=True)
    #print(s_numbers)
    answer = str(int(''.join(s_numbers)))
    return answer
