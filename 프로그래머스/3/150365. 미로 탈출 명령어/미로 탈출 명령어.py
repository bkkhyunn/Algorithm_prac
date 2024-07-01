from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    graph = [[0] * m for _ in range(n)]
    
    dist = abs(x-r) + abs(y-c)
    if k < dist or (k - dist) % 2 != 0:
        return 'impossible'
    
    queue = deque([(x-1, y-1, '', 0)])
    while queue:
        x, y, path, cnt = queue.popleft()
        
        if cnt == k and graph[x][y] == 'E':
            break
        
        dx = [1, 0, 0, -1]
        dy = [0, -1, 1, 0]
        direct = ['d','l','r','u']
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            remain_dist = abs(nx-(r-1)) + abs(ny-(c-1))
            if k - (cnt+1) >= remain_dist:
                queue.append((nx, ny, path+direct[i], cnt+1))
                break
    
    return path