from collections import deque

## bfs
# def solution(info, edges):
#     answer = 0
    
#     graph = {}
#     for i in range(len(info)):
#         graph[i] = []
        
#     for edge in edges:
#         parent, child = edge
#         graph[parent].append(child)
    
#     #print(graph)
    
#     q = deque([[[0], 1, 0]]) # [nodes, sheep, wolf]
#     while q:
#         #print(q[0])
#         nodes, sheep, wolf = q.popleft()
#         answer = max(answer, sheep)
#         node_set = {node:0 for node in nodes}
#         #print(node_set)
#         for node in nodes:
#             for nxt in graph[node]:
#                 n_sheep, n_wolf = sheep, wolf
#                 if nxt not in node_set:
#                     if info[nxt] == 0:
#                         n_sheep += 1
#                     else:
#                         n_wolf += 1
                    
#                     if n_sheep > n_wolf:
#                         q.append([nodes + [nxt], n_sheep, n_wolf])
    
    
#     return answer

## dfs
def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        #print(visited)
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0
                
    visited[0] = 1
    dfs(1, 0)

    return max(answer)