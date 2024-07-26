n = int(input())
matrix = [[0] * 100 for _ in range(100)]

for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            matrix[i][j] = 1
total = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j]:
            total += 1
print(total)