## 공백을 제외하고 두 문장에서 겹치는 가장 긴 부분

def longest_common_substring(A, B):
    A = A.replace(" ", "")
    B = B.replace(" ", "")
    
    n = len(A)
    m = len(B)
    
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    longest = 0
    end_index = 0
    
    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_index = i
    
    # 가장 긴 공통 부분 문자열 추출
    longest_common_substr = A[end_index - longest: end_index]
    
    return longest_common_substr

A = "오늘 먹은 것은 치즈 돈까쓰!!"
B = "치즈 돈까쓰에서는 치즈가 중요해."

result = longest_common_substring(A, B)
print(result)  # "치즈돈까쓰"