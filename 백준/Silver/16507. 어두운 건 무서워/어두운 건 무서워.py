import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]
prefix = [[0] * (c+1) for _ in range(r+1)]

# 누적합 행렬 만들기
for i in range(1, r+1):
    for j in range(1, c+1):
        prefix[i][j] = picture[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(lambda x: int(x), input().split())
    total = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]
    print(total // ((r2-r1+1) * (c2-c1+1)))
        
