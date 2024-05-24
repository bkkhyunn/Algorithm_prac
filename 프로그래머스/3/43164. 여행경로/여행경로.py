from collections import defaultdict

# # dfs - stack
# def solution(tickets):
    
#     graph = defaultdict(list)

#     for (start, end) in tickets:
#         graph[start].append(end)
    
#     # stack 이기 때문에 알파벳 역순으로 정렬하면 순서가 빠른 것부터 빠져나간다.
#     for airport in graph:
#         graph[airport].sort(reverse=True)

#     path = []
#     stack = ["ICN"]
    
#     while stack:
#         # print(stack)
#         # print(graph)
#         # print('---')
        
#         # 현재 위치
#         now = stack[-1]
        
#         # 현재 위치에서 갈 수 있는 곳이 있으면 스택에 넣는다.
#         # 이 때, 다음 행선지가 없는 곳이 들어올 때 defaultdict 에 의하여 default 값인 [] 가 와서 False 처리
#         if graph[now]:
#             next_route = graph[now].pop()
#             stack.append(next_route)
#         # 현재 위치에서 갈 수 있는 곳이 없으면 path에 넣는다.
#         else:
#             path.append(stack.pop())

#     return path[::-1]

# dfs - recursive
def solution(tickets):
    
    graph = defaultdict(list)

    for (start, end) in tickets:
        graph[start].append(end)
        
    for airport in graph.keys():
        graph[airport].sort()
        
    def dfs(graph, path, tickets):
        #print(path)
        if len(path) == len(tickets)+1:
            return path
        
        for i, r in enumerate(graph[path[-1]]):
            
            graph[path[-1]].pop(i)
            
            answer = dfs(graph, path+[r], tickets)
            
            graph[path[-1]].insert(i, r)
            
            if answer:
                return answer
            
    answer = dfs(graph, ['ICN'], tickets)
    return answer
