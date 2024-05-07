def dfs(idx, sheep, wolf, possible):
    global g_info, answer, graph
    if g_info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1
        
    if wolf >= sheep:
        return 
    
    possible.extend(graph[idx])
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])
        
def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for a, b in edges:
        graph[a].append(b)

    dfs(0, 0, 0, [])
    return answer

# from collections import deque

# def solution(info, edges):
#     answer = 0
#     queue = deque()
#     queue.append(0)
    
#     graph = {i:[] for i in range(len(info))}
#     for parent, children in edges:
#         graph[parent].append(children)
        
#     visited = [False] * len(info)
#     sheep, wolf = 0, 0
#     while queue:
#         print(f'queue: {queue}')
#         node = queue.popleft()
#         if not visited[node]:
#             visited[node] = True
#             if node == 0:
#                 sheep += 1
#             else:
#                 wolf += 1
#                 if sheep == wolf:
#                     wolf -= 1
#                     queue.append(parent)
#                     visited[node] = False
#                     continue
#             try:
#                 for j in graph[node]:
#                     parent = node
#                     queue.append(j)
#             except:
#                 print(node, 'error')
    
#     return sheep