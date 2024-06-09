## 완전탐색 - 중복순열
from itertools import product

def solution(word):
    possibles = list()
    spells = ['A','E','I','O','U']
    
    # 가능한 모든 경우의 수 생성
    for j in range(1,6):
        for w in product(spells,repeat=j):
            possibles.append(''.join(w))
            
    # 사전 순으로 정렬
    possibles.sort()
            
    return possibles.index(word) + 1

## 완전탐색 - DFS
def solution(word):
    answer = 0
    spells = ['A','E','I','O','U']
    
    def dfs(spell, word):
        nonlocal answer, spells
        answer += 1
        
        # 만들어진 단어가 주어진 word 와 같으면 True
        if spell == word:
            return True
        
        if len(spell) == 5:
            return False
        
        for s in spells:
            if dfs(spell+s, word):
                return True
        
    for spell in spells:
        if dfs(spell, word):
            return answer
    
    return answer   