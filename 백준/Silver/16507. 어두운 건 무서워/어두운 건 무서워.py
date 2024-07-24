import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [[0] * (c+1)]

for _ in range(r):
    prefix_sum = [0]
    sum_value = 0
    data = list(map(int, input().split()))
    for i in data:
        sum_value += i
        prefix_sum.append(sum_value)
    
    picture.append(prefix_sum)
    
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2-r1+1) * (c2-c1+1)
    total = 0
    for i in range(r1, r2+1):
        total += (picture[i][c2] - picture[i][c1-1 if c1 > 0 else 0])
        
    print(total // cnt)