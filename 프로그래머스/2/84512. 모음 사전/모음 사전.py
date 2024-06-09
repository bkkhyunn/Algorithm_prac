# 중복순열
from itertools import product

def solution(word):
    answer = 0
    possibles = list()
    spells = ['A','E','I','O','U']
    
    for j in range(1,6):
        for i in product(spells,repeat=j):
            possibles.append(list(i))
    # 사전 순으로 만들기
    possibles.sort()
    
    for possible in possibles:
        answer += 1
        w = ''.join(possible)
        if (w == word):
            break
            
    return answer

# dfs