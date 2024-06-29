import sys
sys.setrecursionlimit(int(1e5))
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트노드부터 시작해서 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘어가기
            continue
        parent[y] = x
        
        dfs(y, depth + 1)
        
# A 와 B 의 최소 공통 조상을 찾는 함수
def lca(a, b):

    # 먼저 깊이가 동일하도록 한다. 깊이가 더 큰 쪽을 올린다.
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    # 노드가 같아지도록 거슬러 올라간다.
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a
    
dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
    
    
# DP 를 이용한 개선된 LCA

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21 # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트노드부터 시작해서 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘어가기
            continue
        
        # 2^0. 한칸 위에 있는 부모 정보만 먼저 구한다.
        parent[y][0] = x
        
        dfs(y, depth + 1)
        
# 전체 부모 관계를 설정하는 함수
# 여기서 DP 를 이용해 2의 제곱꼴로 건너 뛰었을 때의 부모값들을 기록한다.
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n+1):
            # j = 3, i = 3 일 때,
            # 3번째 노드의 2^3 위의 부모를 가리킨다.
            # 우항에 parent[parent[3][2]][2] 가 오게 되는데 이는
            # 3번째 노드의 2^2 위의 부모의 2^2 위 부모를 가리키기 때문에
            # 결국 2^3 위 부모를 가리키는 것이다.
            parent[j][i] = parent[parent[j][i-1]][i-1]
        
# A 와 B 의 최소 공통 조상을 찾는 함수
def lca(a, b):

    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a

    # 먼저 깊이가 동일하도록 한다.
    for i in range(LOG-1, -1, -1):
        # << 는 비트단위 시프트 연산자로서, 왼쪽으로 1칸 움직인다는 것이다.
        # 아래 식에서는 i >> 1 이기 때문에 오른쪽으로 1비트 움직이기 때문에 반으로 나눈 값이 된다.
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    
    # 부모가 같아지도록
    if a==b:
        return a
        
    for i in range(LOG-1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]
    
set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
    