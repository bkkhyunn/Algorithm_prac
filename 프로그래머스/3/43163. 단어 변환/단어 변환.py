from collections import deque
# bfs
def solution(begin, target, words):
    answer = 0
    visited = {word:False for word in words}
    graph = {word:[] for word in [begin]+words}
    
    for word1 in graph.keys():
        for word2 in words:
            diff = 0
            for s1, s2 in zip(word1, word2):
                if s1 != s2:
                    diff += 1
            if diff == 1:
                graph[word1].append(word2)
    
    def bfs(word_and_change, graph, visited):
        nonlocal answer
        
        queue = deque(word_and_change)
        
        while queue:
            v, change = queue.popleft()
            
            if target in graph[v]:
                answer = change+1
                break
                
            for w in graph[v]:
                if not visited[w]:
                    visited[w] = True
                    queue.append((w, change+1))

    bfs([(begin, 0)], graph, visited)
                    
    return answer