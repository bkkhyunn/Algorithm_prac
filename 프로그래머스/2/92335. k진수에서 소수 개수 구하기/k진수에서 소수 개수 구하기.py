import math

def is_prime_number(x):
    '''소수 판별 함수'''
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True	      

def solution(n, k):
    answer = []
    
    # 진수 변환
    trans = ''
    while n > 0:
        n, mod = divmod(n, k)
        trans += str(mod)
    trans = trans[::-1]
    
    # 0 을 기준으로 split
    nums = trans.split('0')
    for num in nums:
        if num and is_prime_number(int(num)) and int(num) != 1:
            answer.append(num)
            
    return len(answer)