# 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 일정한 가치의 무게가 정해진 짐들을 배낭에 담을 때, 가치의 합이 최대가 되는 조합을 찾는 알고리즘이다.
# Fractional Knapsack Problem 과 다르게 물건을 쪼갤 수 없는 배낭 문제로, DP 를 활용해 해결 가능하다.

# 점화식
# dp[i][j]=max(dp[i−1][j],dp[i−1][j−s]+v)

# v = 현재 물건의 가치
# s = 현재 물건의 무게
# i = 현재 물건의 순서 번호
# j = 최대 가능 무게

import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
size = [0]
value = [0]
for _ in range(n):
    s, v = map(int, input().strip().split())
    size.append(s)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s = size[i]
    v = value[i]
    for j in range(i, k + 1):
        if j < s:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - s] + v)

print(dp[n][k])