from itertools import product

def solution(N, number):
    
    # N 을 사용한 횟수에 따라 나올 수 있는 경우의 수를 집어 넣는 dp table
    dp = [[] for _ in range(9)]
    dp[1] = [N]
    
    if N == number:
        return 1
    
    for i in range(2, 9):
        
        if (int(str(N)*i)) == number:
            return i
        else:
            dp[i] += [int(str(N)*i)]
        
        for comb in product(range(1, i), range(1, i)):
            if sum(comb) == i:
                for n1 in dp[comb[0]]:
                    for n2 in dp[comb[1]]:
                        possible = [n1+n2, n1-n2, n1*n2, n1//n2]
                        for p in possible:
                            if p>0:
                                if p == number:
                                    return i
                                else:
                                    dp[i] += [p]
        
    return -1