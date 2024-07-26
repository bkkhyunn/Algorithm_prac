n, m = map(int, input().split())

for i in range(2):
    if i == 0:
        a = [list(map(int, input().split())) for _ in range(n)]
    else:
        b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    lst = []
    for j in range(m):
        lst.append(a[i][j] + b[i][j])
    
    for l in lst:
        print(l, end=' ')