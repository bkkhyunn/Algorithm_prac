# 누가 승리하는지 알 수는 없지만, 이기는 경우가 하나라도 생기면 그 중에서 가장 최소값,
# 이기는 경우가 하나도 없으면 패배한 경우 중 가장 최대값을 리턴하면 된다.

def solution(board, aloc, bloc):
    
    def dfs(board, aloc, bloc, turn):
        
        win, lose = set(), set()
        row, col = len(board), len(board[0])
        
        # 상, 하, 좌, 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        if turn % 2 == 0: # A 의 차례
                
            x, y = aloc
            move = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                elif not board[nx][ny]:
                    continue
                else:
                    move.append([nx, ny])
            
            if not move:
                return (not turn % 2 == 0), turn
            
            if aloc == bloc:
                return (turn % 2 == 0), turn + 1
            
            board[x][y] = 0
            for nx, ny in move:
                is_a_win, cnt = dfs(board, [nx, ny], bloc, turn+1)
                if is_a_win:
                    win.add(cnt)
                else:
                    lose.add(cnt)
            board[x][y] = 1
            
        else: # B 차례
                
            x, y = bloc
            move = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                elif not board[nx][ny]:
                    continue
                else:
                    move.append([nx, ny])
            
            if not move:
                return (not turn % 2 == 0), turn
            
            if aloc == bloc:
                return (turn % 2 == 0), turn + 1
            
            board[x][y] = 0
            for nx, ny in move:
                is_a_win, cnt = dfs(board, aloc, [nx, ny], turn+1)
                if is_a_win:
                    lose.add(cnt)
                else:
                    win.add(cnt)
            board[x][y] = 1
            
        if win:                           
            return turn % 2 == 0, min(win)
        else:                             
            return turn % 2 != 0, max(lose)
    
    # board, A 의 위치, B 의 위치, 턴
    _, answer = dfs(board, aloc, bloc, 0)
    
    return answer