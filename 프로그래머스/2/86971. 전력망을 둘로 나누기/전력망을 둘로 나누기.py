# Union-Find
import copy
from collections import Counter

def solution(n, wires):
    answer = 999999
        
    def find(parent, idx):
        if parent[idx] != idx:
            parent[idx] = find(parent, parent[idx])
        return parent[idx]
        
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for i in range(len(wires)):
        n_wires = copy.deepcopy(wires)
        n_wires.pop(i)
        
        parent = [0] * (n+1)
        for j in range(1, n+1):
            parent[j] = j
        
        for a, b in n_wires:
            union(parent, a, b)
        
        for idx in range(len(parent)):
            find(parent, idx)
        
        count = Counter(parent[1:])
        diff = abs(list(count.values())[0] - list(count.values())[1])
        
        answer = min(answer, diff)
    
    return answer