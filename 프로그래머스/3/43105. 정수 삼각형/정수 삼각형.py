def solution(triangle):
    dp = [[0] * len(i) for i in triangle]
    
    for i, elements in enumerate(triangle):
        if i == 0:
            dp[i] = triangle[i]
        
        for j, element in enumerate(elements):
            if j == 0:
                dp[i][j] = element + dp[i-1][j]
            elif j > 0 and j < i:
                dp[i][j] = max((element + dp[i-1][j-1]),(element + dp[i-1][j]))
            elif j == i:
                dp[i][j] = element + dp[i-1][j-1]
    
    return max(dp[-1])