# 'd', 'l', 'r' ,'u' 순으로 가질수록 빠른 경로.
# 따라서 매순간 'd' 부터 차례로 방문한다. 결국 빠른 것부터 선택하기 때문에 그리디의 일종으로 볼 수 있다.
# bfs 를 이용하여 최단경로로 이동하면서 매순간 도착지점과 남은 거리를 계산하여 이동해도 되는 지점으로 이동한다.

from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    graph = [[0] * m for _ in range(n)]
    
    # 이동해야 하는 거리 k 보다 출발지점과 도착지점 사이 거리가 크거나,
    # 왔다갔다 하지 못하는 경우, 'impossible'
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
            
            # 남은 거리 계산. 남은 거리를 계산하지 않고 무작정 큐에 넣으면 시간복잡도를 초과한다.
            remain_dist = abs(nx-(r-1)) + abs(ny-(c-1))
            # 이동해도 되면 큐에 삽입
            if k - (cnt+1) >= remain_dist:
                queue.append((nx, ny, path+direct[i], cnt+1))
                # 이동 가능한지 따지고, 빠른 것부터 넣어주기 때문에 break 해줘도 상관없다.
                break
    
    return path