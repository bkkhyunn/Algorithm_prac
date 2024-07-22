import sys
input = sys.stdin.readline

n, m = map(int, input().split())
buckets = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(lambda x: int(x)-1, input().split())
    buckets[i:j+1] = buckets[i:j+1][::-1]

for i in range(n):
    print(buckets[i], end=' ')