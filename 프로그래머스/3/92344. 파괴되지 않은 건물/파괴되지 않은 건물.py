# 누적합 사용
# 효율성 테스트를 통과하기 위해서 값을 갱신하는 부분의 시간 복잡도를 줄여야 한다.
# 이를 위해 O(NM) 이 걸릴 수 있던 시간 복잡도를 누적합을 사용해서 O(1) 로 줄인다.

import numpy as np

def solution(board, skill):

    n = len(board)
    m = len(board[0])
    prefix_sum = np.zeros((n+1, m+1))
    
    for tp, r1, c1, r2, c2, degree in skill:
        
        degree = -degree if tp == 1 else degree
            
        prefix_sum[r1][c1] += degree
        prefix_sum[r1][c2+1] -= degree
        prefix_sum[r2+1][c1] -= degree
        prefix_sum[r2+1][c2+1] += degree
    
    # 행방향 누적합
    for i in range(n):
        for j in range(1, m):
            prefix_sum[i][j] += prefix_sum[i][j-1]
    
    # 열방향 누적합
    for j in range(m):
        for i in range(1, n):
            prefix_sum[i][j] += prefix_sum[i-1][j]
    
    return sum([int(board[i][j] + prefix_sum[i][j]) > 0 for j in range(m) for i in range(n)])