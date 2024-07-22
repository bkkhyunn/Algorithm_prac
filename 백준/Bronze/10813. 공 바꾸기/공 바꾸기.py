import sys
input = sys.stdin.readline

n, m = map(int, input().split())
buckets = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    buckets[i-1], buckets[j-1] = buckets[j-1], buckets[i-1]

for i in range(n):
    print(buckets[i], end=' ')