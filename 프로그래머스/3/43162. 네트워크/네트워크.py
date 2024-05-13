from collections import deque

# bfs
def solution(n, computers):
    answer = 1
    queue = deque([0])
    visited = [False] * len(computers)
    while queue:
        idx = queue.popleft()
        visited[idx] = True
        for i, computer in enumerate(computers[idx]):
            if (not visited[i]) and computer == 1:
                queue.append(i)
        
        if not len(queue) and (False in visited):
            answer += 1
            for i, visit in enumerate(visited):
                if not visit:
                    queue.append(i)
                    break
        
    return answer