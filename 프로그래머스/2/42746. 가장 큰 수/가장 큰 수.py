import functools

# 기억해두면 좋은 풀이
def comparator(a,b):
    '''
    functools.cmp_to_key(func)는 sorted()와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는
    함수이다. 단, func() 함수는 두 개의 인수를 입력하여 첫 번째 인수를 기준으로 그 둘을 비교하고 작으면 음수, 같으면 0,
    크면 양수를 반환하는 비교 함수이어야 한다.
    '''
    t1 = a+b
    t2 = b+a
    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# 내 풀이
def solution(numbers):
    s_numbers = [str(n) for n in numbers]
    # 1000 이하의 원소이기 때문에 3을 곱해주면 '000' 식이 되고
    # 거기서 정렬하면 한자리 수와 같은 수의 두, 세자리 수의 크기를 비교하기 용이하다.
    # 3, 30 에서 3이 크게 되고, 3, 34 에서는 34가 크게 된다.
    s_numbers.sort(key=lambda x: x*3, reverse=True)
    #print(s_numbers)
    answer = str(int(''.join(s_numbers)))
    return answer