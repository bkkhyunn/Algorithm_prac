import sys
input = sys.stdin.readline

n, m = map(int, input().split())
buckets = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        buckets[idx-1] = str(k)
        
for i in buckets:
    print(i, end = ' ')