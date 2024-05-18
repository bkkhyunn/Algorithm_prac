import numpy as np
import copy

# 좌표를 회전 시키는 함수
def rotate(maps, i):
    nmap = np.array(maps)
    return np.rot90(nmap, i)

# 모든 figure 의 첫 시작(맨 위의 맨 좌측)을 (0,0) 으로 맞추고 비교 용이하도록
def normalize(coords):
    min_x = min(coord[0] for coord in coords)
    min_y = min(coord[1] for coord in coords)
    return [(coord[0] - min_x, coord[1] - min_y) for coord in coords]

# table 의 도형들을 회전시키면서 figure 를 얻는다.
def make_figure(table, i):

    def dfs(coord, maps):
        nonlocal figure
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        x, y = coord
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps):
                continue
            
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny]:
                maps[nx][ny] = 0
                figure = figure+[(nx, ny)]
                dfs((nx, ny), maps)
                
        return figure
    
    figures = []
    maps = rotate(table, i)
    
    for x in range(len(table)):
        for y in range(len(table[0])):
            if maps[x][y]:
                maps[x][y] = 0
                figure = [(x,y)]
                figure = dfs((x,y), maps)
                if len(figure) >= 1:
                    figures.append(figure)
    
    return figures

def solution(game_board, table):
    answer = 0
    l = len(game_board)
    
    # game_board 를 돌면서 puzzle 이 들어갈 공간을 찾는다.
    def dfs(coord, maps):
        nonlocal puzzle
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        x, y = coord

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps):
                continue
            
            if maps[nx][ny] == 1:
                continue
                
            if maps[nx][ny] == 0:
                maps[nx][ny] = 1
                puzzle += [(nx, ny)]
                
                dfs((nx, ny), maps)
                
        return puzzle
    
    cnt = 0
    for i in range(4):
        # table 을 회전시켜가며 가지고 있는 figure 를 찾는다.
        #print(table)
        figures = make_figure(table, i)
        # game_board 와 table 의 비교를 용이하게 할 수 있도록 normalize
        n_figures = list(map(normalize, figures))
        maps = copy.deepcopy(game_board)
        #print(maps)
        #print(figures)
        #print(n_figures)
        puzzles = []
        for x in range(l):
            for y in range(l):
                if not maps[x][y]:
                    maps[x][y] = 1
                    puzzle = [(x,y)]
                    puzzle = dfs((x,y), maps)
                    if len(puzzle) >= 1:
                        puzzles.append(puzzle)
        #print(puzzles)
        n_puzzles = list(map(normalize, puzzles))
        # print(n_puzzles)
        # print(n_figures)
        for ti, f in enumerate(n_figures):
            if f in n_puzzles:
                cnt += len(f)
                gi = n_puzzles.index(f)
                #print(figures[j])
                for px, py in puzzles[gi]:
                    game_board[px][py] = 1
                puzzles.pop(gi)
                n_puzzles.pop(gi)
                table = rotate(table, i)
                for tx, ty in figures[ti]:
                    table[tx][ty] = 0
                table = rotate(table, 4-i)
                        
    answer = cnt
    
    return answer