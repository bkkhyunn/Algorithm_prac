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