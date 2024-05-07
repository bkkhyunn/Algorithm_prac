# import numpy as np

# def spatial(point, l, nboard):
#     return np.sum(nboard[point[0]:point[0]+l, point[1]:point[1]+l])

# def solution(board):
#     answer = 0
#     nboard = np.array(board)
#     for x, b in enumerate(board):
#         for y, c in enumerate(b):
#             limit = min(len(b)-y, len(board)-x)
#             for l in range(1, limit+1):
#                 spatial_res = spatial((x,y), l, nboard)
#                 #print(x, y, l, spatial_res)
#                 if spatial_res == l**2:
#                     answer = max(answer, spatial_res)
#     return int(answer)

def solution(board):
    n = len(board)
    m = len(board[0])

    # dp 준비
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]
    
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    return answer**2