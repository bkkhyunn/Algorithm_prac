from collections import deque

# bfs
def solution(maps):
    
    # 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y):
        queue = deque([(x,y)])
        
        while queue:
            x, y = queue.popleft()
            # 동, 서, 남, 북 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # map 밖으로 넘어가는 경우 skip
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue
                # 이동할 수 있다면 큐에 이동 좌표를 넣고, 해당 좌표에 거리 계산
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
    bfs(0,0)
    
    return -1 if maps[-1][-1] == 1 else maps[-1][-1] 