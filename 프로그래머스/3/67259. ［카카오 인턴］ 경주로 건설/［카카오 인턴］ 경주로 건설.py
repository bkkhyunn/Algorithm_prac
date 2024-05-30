# dfs - stack + DP
# 탐색 방향(up, down, left, right)의 조합에 따라 정답이 될수도 안될수도 있는 문제이다.
# 다익스트라로는 문제가 해결되지 않는다. 가장 비용이 적은 길을 골랐는데, 최종 목적지까지 코너가 생기면 결국엔 더 큰 비용이
# 될 수도 있기 때문이다.
# 따라서 좌표별로 cost 를 같이 기록하고, 기록된 cost 가 해당 좌표로 도달할 수 있는 방향만큼 모두 기록하도록 해서
# 모든 경우를 구하도록 하면 완벽한 정답을 구할 수 있을 것 같다.

def solution(board):
    
    # board 에 cost 까지 넣어두기
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = [board[i][j], 0]
    
    # x, y, cost, direct
    stack = [(0,0,0,'')]
    
    board[0][0] = [1, 0]
    costs = []
    
    while stack:
        #print(stack)
        x, y, cost, direct = stack.pop()
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        di = ['u','l','d','r']
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ndirect = di[i]
            
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue
            
            
            if direct == '':
                if not board[nx][ny][0]:
                    board[nx][ny] = [1, cost+100]
                    stack.append((nx, ny, cost+100, ndirect))
                
            else:
                if direct != ndirect:
                    if nx == len(board)-1 and ny == len(board)-1:
                        costs.append(cost+600)
                        board[x][y][1] = 1000000
                        continue
                    # 방문하지 않았거나, 기존 cost 보다 새로운 cost 가 더 쌀 때
                    if not board[nx][ny][0] or board[nx][ny][1] >= cost+600:
                        board[nx][ny] = [1, cost+600]
                        stack.append((nx, ny, cost+600, ndirect))
                    
                else:
                    if nx == len(board)-1 and ny == len(board)-1:
                        costs.append(cost+100)
                        board[x][y][1] = 10000000
                        continue
                    # 방문하지 않았거나, 기존 cost 보다 새로운 cost 가 더 쌀 때
                    if not board[nx][ny][0] or board[nx][ny][1] >= cost+100: 
                        board[nx][ny] = [1, cost+100]
                        stack.append((nx, ny, cost+100, ndirect))
    #print(board)
    return min(costs)