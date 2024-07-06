## 해밀턴 경로

def hamiltonian_path(graph):
    n = len(graph)
    path = [-1] * n  # 경로를 저장할 배열
    visited = [False] * n  # 방문 여부를 저장할 배열

    # pos는 현재 경로에서 몇 번째 정점을 방문하고 있는지를 나타낸다.
    # 재귀 함수 hamiltonian_util이 호출될 때마다 pos가 1씩 증가하며, 모든 정점을 방문했는지 확인.
    # path 배열의 pos 위치에 현재 방문한 정점을 기록

    def is_valid(v, pos):
        # v가 현재위치(pos)에서 유효한 정점인지 확인한다.
        if not visited[v]:
            # 방문하지 않은 정점이고 전 위치(pos-1)에서 현재정점(v)로의 간선이 있으면 유효하다.
            if pos == 0 or graph[path[pos-1]][v]:
                return True
        return False

    def hamiltonian_util(pos):
        '''
        백트래킹을 사용하여 모든 정점을 방문하는 경로를 찾는다.
        재귀적으로 호출하여 경로를 찾고, 실패하면 이전 상태로 돌아간다.
        '''
        # 모든 정점을 방문한 경우 해밀턴 경로를 찾은 것
        if pos == n:
            return True

        for v in range(1, n):  # 시작 정점은 0이므로 1부터 시작
            if is_valid(v, pos):
                path[pos] = v
                visited[v] = True

                if hamiltonian_util(pos + 1):
                    return True

                # Back tracking
                path[pos] = -1
                visited[v] = False

        return False

    # 시작 정점 0. -> 해밀턴 경로가 존재하지 않으면 다른 정점에서 시작해봐야 할 수도 있다.
    path[0] = 0
    visited[0] = True

    if not hamiltonian_util(1):
        print("해밀턴 경로가 없다.")
        return False

    print("해밀턴 경로:", path)
    return True

# 예제
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

hamiltonian_path(graph)


## 해밀턴 회로

def hamiltonian_circuit(graph):
    n = len(graph)
    path = [-1] * n  # 경로를 저장할 배열
    visited = [False] * n  # 방문 여부를 저장할 배열

    def is_valid(v, pos):
        # v가 pos 위치에서 유효한 정점인지 확인
        if not visited[v]:
            # pos-1에서 v로의 간선이 있으면 유효
            if pos == 0 or graph[path[pos-1]][v]:
                return True
        return False

    def hamiltonian_util(pos):
        # 모든 정점을 방문한 경우 해밀턴 회로를 찾은 것
        if pos == n:
            # 경로를 찾는 과정은 해밀턴 경로와 유사하지만, 마지막에 시작 정점으로 돌아오는 조건을 추가
            # 시작 정점으로 돌아오는지 확인
            if graph[path[pos-1]][path[0]]:
                return True
            else:
                return False

        for v in range(1, n):  # 시작 정점은 0이므로 1부터 시작
            if is_valid(v, pos):
                path[pos] = v
                visited[v] = True

                if hamiltonian_util(pos + 1):
                    return True

                # Backtrack
                path[pos] = -1
                visited[v] = False

        return False

    # 시작 정점을 0
    path[0] = 0
    visited[0] = True

    if not hamiltonian_util(1):
        print("해밀턴 회로가 없습니다.")
        return False

    print("해밀턴 회로:", path + [path[0]])
    return True

# 예제
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

hamiltonian_circuit(graph)