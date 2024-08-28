A = input()
B = input()

def longest_common_substring(A, B):
    A = A.replace(" ", "")
    B = B.replace(" ", "")
    
    n = len(A)
    m = len(B)
    
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return max(map(max,dp))

print(longest_common_substring(A, B))