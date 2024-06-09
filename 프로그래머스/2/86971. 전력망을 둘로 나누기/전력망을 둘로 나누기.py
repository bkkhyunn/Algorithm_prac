# Union-Find
import copy
from collections import Counter

def solution(n, wires):
    answer = 999999
    
    # 특정 노드가 속한 집합 찾기
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    # 두 노드가 속한 집합 합치기
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    # wires 에서 하나씩 끊으며 완전탐색
    for i in range(len(wires)):
        n_wires = copy.deepcopy(wires)
        n_wires.pop(i)
        
        # 부모 테이블 초기화
        parent = [0] * (n+1)
        for j in range(1, n+1):
            parent[j] = j
        
        # 간선 정보를 가지고 Union 수행
        for a, b in n_wires:
            union(parent, a, b)
        
        # 부모 테이블 자체에는 부모 노드만 설정되어 있기 때문에 루트 노드로 갱신이 필요하다.
        # 즉 각 노드가 속한 집합의 루트 노드로 최신화하는 것이다.
        for idx in range(1, n+1):
            find(parent, idx)
        
        count = Counter(parent[1:])
        diff = abs(list(count.values())[0] - list(count.values())[1])
        
        answer = min(answer, diff)
    
    return answer