# 완전탐색 - 중복순열
from itertools import product

def solution(word):
    possibles = list()
    spells = ['A','E','I','O','U']
    
    for j in range(1,6):
        for w in product(spells,repeat=j):
            possibles.append(''.join(w))
            
    # 사전 순으로 정렬
    possibles.sort()
            
    return possibles.index(word) + 1

# 완전탐색 - DFS
# def solution(word):
#     answer = 0
#     spells = ['A','E','I','O','U']
    
#     def dfs():
        
        
#     return answer
    