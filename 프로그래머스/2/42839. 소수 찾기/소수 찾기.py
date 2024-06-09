def solution(numbers):
    answer = 0
    numbers = list(numbers)
    visited = [False] * len(numbers)
    prime = []
    
    # 소수 판별 함수
    def is_prime_number(x):
        if x <= 1:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    
    def dfs(number, numbers):
        nonlocal answer, visited, prime
        
        if number != '' and (int(number) not in prime) and is_prime_number(int(number)):
            #print(number)
            prime.append(int(number))
            answer += 1
        
        for i, n in enumerate(numbers):
            if not visited[i]:
                visited[i] = True
                dfs(number+n, numbers)
                visited[i] = False
                
    dfs('', numbers)
    return answer