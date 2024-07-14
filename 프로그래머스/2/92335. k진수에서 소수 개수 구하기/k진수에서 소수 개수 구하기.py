import math
import re

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True	      

def solution(n, k):
    answer = []
    trans = ''
    while n > 0:
        n, mod = divmod(n, k)
        trans += str(mod)
    trans = trans[::-1]
    
    patterns = ['([1-9]+0)', '(0[1-9]+)', '(0[1-9]+0)', '([1-9]+)']
    for pattern in patterns:
        finds = re.findall(pattern, trans)
        for find in finds:
            num = find.replace('0', '')
            if num and is_prime_number(int(num)) and int(num) != 1:
                answer.append(find)
                trans = trans.replace(find, '', 1)
    
    return len(answer)