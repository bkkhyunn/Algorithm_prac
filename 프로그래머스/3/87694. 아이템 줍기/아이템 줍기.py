from collections import deque
import numpy as np
# bfs
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = np.zeros((102,102))
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        # 테두리
        maps[x1:x2+1, y1:y2+1] = 1
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        # 내부
        maps[x1+1:x2, y1+1:y2] = 0
        
    start = (characterX * 2, characterY * 2)
    end = (itemX * 2, itemY * 2)
    
    def bfs(start, maps):
        nonlocal end, answer
        
        queue = deque(start)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while queue:
            #print(queue)
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= 102 or ny >= 102:
                    continue
                
                if maps[nx][ny] == 0:
                    continue
                    
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    bfs([start], maps)
    answer = (maps[end[0]][end[1]]) // 2
    return answer