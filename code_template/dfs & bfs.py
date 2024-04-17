# 현재 위치에서의 각 앞/뒤 문자와, 앞뒤 문자열의 같은 인덱스에 해당하는 문자 확인
# ex. ["X591X","X1X5X","X231X", "1XXX1"] 여기서, 현재 위치가 5일 경우,
# 2차원 배열을 만들어 탐색
# ----------------------------------------------------------------

from collections import deque

def solution(maps):
    answer = []
    
    # maps 1차원 -> 2차원
    maps = list(list(i) for i in maps)  # maps = [["X","5","9","1","X"],["X","1","X","5","X"],["X","2","3","1","X"],["1","X","X","X","1"]]
    
    def bfs(x,y):
        if (maps[x][y] == 'X'):     # 현재 위치 = '바다' (='X')면, 0 반환
            return 0
        
        queue = deque()             # 빈 큐 생성
        queue.append([x,y])         # 큐에 현재 위치 추가
        days = 0                    # days: 머무를 수 있는 날짜를 저장할 변수
        
        if not arr[x][y]:           # 바다 외 무인도 첫 탐색
            arr[x][y] = True        # True: 해당 위치를 탐색함
            days += int(maps[x][y]) # 머무를 수 있는 날을 더함
            
        while queue:
            x, y = queue.popleft()  # 현재 큐에 담겨있는 위치 x,y에 넣어줌
            for i in range(len(move)):  # 현재 위치에서 이동 가능한 방향에 따라 다음 위치 탐색
                new_x = x + move[i][0]  # 다음 위치 각각 저장
                new_y = y + move[i][1]
                
                if (0 <= new_x < len(maps)) and (0 <= new_y < len(maps[0])):  # 만약 새로운 위치가 이동 가능하고,
                    if (not arr[new_x][new_y]):                               # 처음 탐색하는 곳이면,
                        arr[new_x][new_y] = True                              # True 반환 (=탐색함)
                        
                        if (maps[new_x][new_y] != 'X'):                       # 바다가 아니면,
                            queue.append([new_x, new_y])                      # 새로운 위치로 이동하고
                            days += int(maps[new_x][new_y])                   # 머무를 수 있는 날을 더함               
        return days
    
# ----------------------------------------------
    arr = []        # 각 위치를 지나왔는지 확인할 리스트 생성 (True/False)
    for i in range(len(maps)):
        lst = []
        for i in range(len(maps[0])):
            lst.append(False)
        arr.append(lst)

    # 위 구문을 아래와 같이 더 간결하게 표현 가능
    # arr = list(list(False for i in range(len(maps[0]))) for i in range(len(maps)))

    move = [[0, -1], [0, 1], [1, 0], [-1, 0]]   # 상하좌우 방향 저장
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            result = bfs(i, j)      # 위에서 정의한 bfs로 무인도 탐색
            if (result != 0):       # days를 answer 리스트에 추가
                answer.append(result)
            
    if (len(answer) == 0):          # 무인도가 존재하지 않으면, -1 저장
        answer = [-1]
    else:
        answer.sort()               

    return answer