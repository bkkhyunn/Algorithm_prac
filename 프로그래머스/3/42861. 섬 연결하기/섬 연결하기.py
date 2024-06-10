# 최소 신장 트리 - 크루스칼 알고리즘

def solution(n, costs):
    
    parent = [0] * n
    
    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges, result = [], 0
    
    for a, b, cost in costs:
        edges.append((cost, a, b))
    
    edges.sort()
    
    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i
    
    def find_parent(parent, x):
        # 루트 노드를 찾을 때까지 재귀 호출.
        if parent[x] != x:
            # 경로 압축
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    # 간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    return result