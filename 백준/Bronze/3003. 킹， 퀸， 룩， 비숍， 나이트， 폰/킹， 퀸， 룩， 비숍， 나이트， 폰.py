chess = [1, 1, 2, 2, 2, 8]
find = list(map(int, input().split()))

for c, f in zip(chess, find):
    print(c-f, end=' ')