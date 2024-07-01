# 삼각형이 한개씩 생길 때마다 그 전의 경우의 수를 이용해 구할 수 있다. 따라서 DP 로 접근
# dp 점화식
# 윗변과 맞닿은 삼각형이 생기는 때는 3의 배수일 때.
# if (n-4) % 3 == 0 일 때 dp_n = dp_{n-1} + dp_{n-3}
# if (n-4) % 3 != 0 일 때 dp_n = dp_{n-1} + dp_{n-2}
# 미리 10007 로 나누어 DP 를 관리해서 메모리를 줄인다.

def solution(n, tops):

    total = (2*n+1) + len(tops)
    dp = [0] * (total+1)
    
    for i in range(1, total+1):
        if i <= 2:
            dp[i] = dp[i-1] + 1
            continue
        
        # 윗변에 삼각형이 없다면
        if (i-3) % 3 == 0 and tops[(i-3)//3] == 0:
            dp[i] = dp[i-1]
            continue
        
        # 좌측 하단 삼각형이 생길 때, 그 삼각형을 포함한 마름모는 3단계 전 경우의 수이다.
        if (i-4) % 3 == 0:
            dp[i] = (dp[i-1] + dp[i-3]) % 10007
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 10007
            
    return dp[-1]