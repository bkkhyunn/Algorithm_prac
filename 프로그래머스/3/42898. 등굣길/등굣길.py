# bfs 로 풀려했으나,
# 1. 방문한 곳은 방문하지 않는 특성때문에 복잡해진다.
# 2. 방문 테이블을 따로 두지 않으면 2^nm 이 되어 효율성 테스트 통과 못한다.
# 점화식은 매 셀마다 도달할 수 있는 경로를 모두 기입하고, c_n,m = c_n-1,m + c_n,m-1

def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:                 
                dp[1][1] = 1
            elif dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
    return dp[n][m] % 1000000007