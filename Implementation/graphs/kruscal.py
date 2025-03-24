# 최소 신장 트리 알고리즘.
# 대표적으로 크루스칼 알고리즘이 있다.

# 기본적으로 두 원소가 서로 같은 집합인지 아닌지를 판단하기 위해서 서로소 집합 자료구조 사용
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출. 경로 압축 사용
    if parent[x] != x:
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
        
def kruskal(v, edges):
    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    parent = [i for i in range(v+1)]
    # 간선을 비용 순으로 정렬
    edges.sort()
    result = 0

    # 간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    return result
        
# 노드의 개수 v, 간선 edges
v = 4  # Number of nodes
edges = [
    (1, 1, 2),
    (3, 1, 3),
    (3, 2, 3),
    (6, 2, 4),
    (2, 3, 4)
]

print("Kruskal's MST cost:", kruskal(v, edges))