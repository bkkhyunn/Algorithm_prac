# 특정 원소가 속한 집합을 찾기 -> 루트 노드를 반환한다.
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 특정 원소가 속한 집합을 찾기(경로 압축)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # 부모 테이블 값을 루트 노드로 바로 갱신
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수 v, 간선(Union 연산)의 개수 e
v, e = 100, 100

# 부모 테이블 초기화하기
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력 -> 그 집합의 루트 노드를 출력한다. 루트가 같으면 같은 집합이다.
# 부모 테이블의 내용을 출력했을 때 자신의 루트가 나오지 않고 바로 위 부모가 나올 수 있는데, find_parent 를 한 번 더 거쳐주어 갱신할 수 있다.
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

# 부모 테이블 내용 출력 -> 자신의 루트, 집합에 대한 정보가 아닐 수 있다.
for i in range(1, v+1):
    print(parent[i], end=' ')
    
    
# 사이클 판별 알고리즘
# 특정 원소가 속한 집합을 찾기 (경로 압축)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # 부모 테이블 값을 루트 노드를 갖도록 바로 갱신
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수 v, 간선(Union 연산)의 개수 e

# 부모 테이블 초기화하기
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# Cycle 발생 여부
cycle = False

for i in range(e):
    a, b = map(int(), input().split())
    
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    # 즉 노드 a 와 노드 b 가 같은 집합에 속해있지 않다면 같은 집합에 속하도록 합집합 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생하지 않음")