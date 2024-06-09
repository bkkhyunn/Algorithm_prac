# 완전 탐색 - 순열
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for possible in permutations(dungeons, len(dungeons)):
        tired = k
        clear = 0
        
        for dungeon in possible:
            required, consumption = dungeon
            
            if required <= tired and tired >= consumption:
                tired -= consumption
                clear += 1
                
        answer = max(answer, clear)
        
    return answer

# 완전 탐색 - DFS, 백트래킹
def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(k, cnt, dungeons):
        nonlocal answer, visited
        
        if cnt > answer:
            answer = cnt

        for idx in range(len(dungeons)):
            
            if k >= dungeons[idx][0] and not visited[idx]:
                visited[idx] = True
                dfs(k - dungeons[idx][1], cnt+1, dungeons)
                # 백트래킹
                visited[idx] = False
                
    dfs(k, 0, dungeons)
    return answer