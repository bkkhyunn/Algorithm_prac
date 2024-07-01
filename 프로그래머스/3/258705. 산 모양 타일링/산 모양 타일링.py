# dp 점화식
# 윗변과 맞닿은 삼각형이 생기는 때는 3의 배수일 때.
# if (n-4) % 3 == 0 일 때 dp_n = dp_{n-1} + dp_{n-3}
# if (n-4) % 3 != 0 일 때 dp_n = dp_{n-1} + dp_{n-2}

def solution(n, tops):

    total = (2*n+1) + len(tops)
    
    dp = [0] * (total+1)
    
    for i in range(1, total+1):
        if i <= 2:
            dp[i] = dp[i-1] + 1
            continue
            
        if (i-3) % 3 == 0 and tops[(i-3)//3] == 0:
            dp[i] = dp[i-1]
            continue
        
        if (i-4) % 3 == 0:
            dp[i] = (dp[i-1] + dp[i-3]) % 10007
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 10007
            
    return dp[-1]