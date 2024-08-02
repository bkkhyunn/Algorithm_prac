n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

print((max(xs)-min(xs)) * (max(ys)-min(ys)))