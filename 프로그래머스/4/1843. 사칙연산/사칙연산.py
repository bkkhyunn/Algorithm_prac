# 점화식
# DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
# 그러나 빼기(-) 연산이 있기 때문에, 최대값을 만드려면 빼는 값이 최소값이 되어야 한다. 따라서 최소값을 담는 DP 도 필요하다.
# MAX_DP[i][j] = i번째 부터 j번째까지 구간의 연산의 최댓값
# MIN_DP[i][j] = i번째 부터 j번째까지 구간의 연산의 최솟값

def solution(arr):
    # 숫자의 개수
    n = len(arr) // 2 + 1
    # 최대값, 최소값 DP
    max_dp = [[-100000000] * n for _ in range(n)]
    min_dp = [[100000000] * n for _ in range(n)]
    
    # 한 번 연산할 때 사용하는 숫자의 개수. 즉 step = i-j 다.
    for step in range(n):
        # i 부터 j 까지의 연산을 수행한다.
        for i in range(n-step):
            j = i + step
            
            if step == 0:
                max_dp[i][i] = int(arr[i*2])
                min_dp[i][i] = int(arr[i*2])
                
            else:
                for k in range(i, j):
                    if arr[k*2+1] == '+':
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                    else:
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
        
    return max_dp[0][-1]