from collections import deque

# bfs
# def solution(n, computers):
#     answer = 1
#     queue = deque([0])
#     visited = [False] * n
#     while queue:
#         idx = queue.popleft()
#         visited[idx] = True
#         for i, computer in enumerate(computers[idx]):
#             if (not visited[i]) and computer == 1:
#                 queue.append(i)
#         if len(queue) == 0 and (False in visited):
#             answer += 1
#             for i, visit in enumerate(visited):
#                 if not visit:
#                     queue.append(i)
#                     break
#     return answer

# bfs 좀 더 깔끔한 풀이
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(computers, start, visited):
        queue = deque([start])
        # 현재 노드 방문 처리
        visited[start] = True
        
        while queue:
            # 현재 노드
            v = queue.popleft()
            for i in range(n):
                # 현재 노드와 연결되어 있고, 방문하지 않은 노드이면 방문 처리 하고 큐에 삽입
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    # 방문 하지 않은 노드들을 돌아가면서 bfs
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(computers, i, visited)
            
    return answer