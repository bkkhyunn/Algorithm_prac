# dfs - stack
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
            
            # 방문하지 않았거나, 기존 cost 보다 새로운 cost 가 더 쌀 때
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
                    if not board[nx][ny][0] or board[nx][ny][1] >= cost+600:
                        board[nx][ny] = [1, cost+600]
                        stack.append((nx, ny, cost+600, ndirect))
                    
                else:
                    if nx == len(board)-1 and ny == len(board)-1:
                        costs.append(cost+100)
                        board[x][y][1] = 10000000
                        continue
                    if not board[nx][ny][0] or board[nx][ny][1] >= cost+100: 
                        board[nx][ny] = [1, cost+100]
                        stack.append((nx, ny, cost+100, ndirect))
    #print(board)
    return min(costs)