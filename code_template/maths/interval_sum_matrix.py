# 데이터 (5x5 행렬)
r, c = 5, 5
data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# Prefix Sum(누적 합) 계산
prefix_sum = [[0] * (c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        prefix_sum[i][j] = data[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    
# Interval Sum(구간 합) 계산
r1, c1, r2, c2 = map(int, input().split())
print(prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1])