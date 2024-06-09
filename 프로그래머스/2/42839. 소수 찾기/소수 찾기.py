# 소수 판별 함수
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# DFS - 백트래킹
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    visited = [False] * len(numbers)
    prime = set()
    
    def dfs(number, numbers):
        nonlocal answer, visited, prime
        
        if number != '' and (int(number) not in prime) and is_prime_number(int(number)):
            #print(number)
            prime.add(int(number))
            answer += 1
        
        for i, n in enumerate(numbers):
            if not visited[i]:
                visited[i] = True
                dfs(number+n, numbers)
                # 백트래킹
                visited[i] = False
                
    dfs('', numbers)
    return answer

# 순열
from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    prime = set()
    
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            number = ''.join(perm)
            #print(number)
            if (int(number) not in prime) and is_prime_number(int(number)):
                prime.add(int(number))
                answer += 1
                
    return answer