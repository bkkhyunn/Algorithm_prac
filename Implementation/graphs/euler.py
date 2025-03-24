# 무향 그래프에서의 오일러 경로 or 오일러 회로 찾기
from collections import defaultdict

def find_eulerian_path_or_circuit_undirected(graph):
    # 간선을 추가하는 함수
    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    # 정점의 차수 초기화
    degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            degree[u] += 1

    # 시작 정점 찾기 - 홀수 차수를 가진 정점(오일러 경로) 또는 임의의 정점(오일러 회로)
    start_node = None
    odd_count = 0
    for node in graph:
        if degree[node] % 2 != 0:
            odd_count += 1
            if start_node is None:
                start_node = node

    # 그래프가 유효한 오일러 경로 또는 회로를 갖고 있는지 확인
    if odd_count != 0 and odd_count != 2:
        return None

    # 홀수 차수가 없는 경우 임의의 정점을 시작 정점으로 설정
    if start_node is None:
        start_node = next(iter(graph))

    # 방문 여부를 체크하기 위한 set
    visited = set()

    # 연결 그래프인지 확인하는 DFS
    def dfs(node):
        stack = [node]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

    # 시작 정점부터 DFS를 수행하여 연결된 모든 정점을 방문.
    visited.add(start_node)
    dfs(start_node)

    # 모든 정점을 방문했는지 확인
    for node in graph:
        if node not in visited:
            return None  # 연결되지 않은 정점이 있으면 오일러 경로나 회로가 없음

    # 방문된 간선을 추적하기 위해 사용되는 set
    visited_edges = set()
    
    # Hierholzer's Algorithm
    stack = [start_node]
    path = []

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u][-1]
            edge = (min(u, v), max(u, v))  # 정렬된 간선 사용 -> 추적에 용이
            if edge not in visited_edges:
                visited_edges.add(edge)
                stack.append(v)
                graph[u].pop()
                graph[v].remove(u)  # 무향 그래프이므로 양방향 간선을 제거
            else:
                stack.pop()
        else:
            path.append(stack.pop())

    # 경로 반환
    return path[::-1]

# 예제
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

result = find_eulerian_path_or_circuit_undirected(graph)
if result is None:
    print("오일러 경로 또는 회로가 없다.")
else:
    print("오일러 경로 또는 회로:", result)


# 유향 그래프에서의 오일러 경로 or 오일러 회로 찾기
from collections import defaultdict

def find_eulerian_path_or_circuit_directed(graph):
    # 정점의 진입 차수와 진출 차수를 계산
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    for u in graph:
        out_degree[u] = len(graph[u])
        for v in graph[u]:
            in_degree[v] += 1

    # 시작 정점과 끝 정점을 찾기
    start_node, end_node = None, None
    for node in graph:
        if in_degree[node] == out_degree[node] + 1:
            if end_node is not None:
                return None  # 오일러 경로가 두 개 이상 존재하는 경우
            end_node = node
        elif out_degree[node] == in_degree[node] + 1:
            if start_node is not None:
                return None  # 오일러 경로가 두 개 이상 존재하는 경우
            start_node = node
        elif out_degree[node] != in_degree[node]:
            return None  # 오일러 경로가 존재하지 않는 경우

    # 시작 정점이 없는 경우 임의의 정점을 시작 정점으로 설정
    if start_node is None:
        start_node = next(iter(graph))

    # Hierholzer's Algorithm
    def dfs(node):
        while graph[node]:
            neighbor = graph[node].pop(0)
            dfs(neighbor)
        path.append(node)

    # Hierholzer's Algorithm을 시작 정점에서 호출
    path = []
    dfs(start_node)

    # 경로 반환
    return path[::-1] if len(path) == sum(out_degree.values()) + 1 else None

# 예제
graph = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [4],
    4: [1]
}

result = find_eulerian_path_or_circuit_directed(graph)
if result is None:
    print("오일러 경로 또는 회로가 없습니다.")
else:
    print("오일러 경로 또는 회로:", result)
