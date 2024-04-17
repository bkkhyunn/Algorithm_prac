from collections import deque

def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            # 해당 iter 에서 출발 좌표
            x, y = queue.popleft()
            
            # 가야할 방향 결정
            for i in range(4):
                
                # 새로 가야할 좌표 설정
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵을 넘어가면 pass
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                
                # 벽이면 pass
                if maps[nx][ny] == 0:
                    continue

                # 벽이 아니니까 go
                if maps[nx][ny] == 1:
                    
                    # 실제 움직인 거리를 counting 하면서 움직임
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
                # if maps[len(maps)-1][len(maps[0])-1] > 1:
                #     return maps[len(maps)-1][len(maps[0])-1]
                
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer