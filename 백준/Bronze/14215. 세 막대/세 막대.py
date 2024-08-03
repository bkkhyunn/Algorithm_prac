a, b, c = map(int, input().split())
edges = [a, b, c]
edges.sort()

if edges[2] >= edges[0] + edges[1]:
    edges[2] = edges[0] + edges[1] - 1
print(sum(edges))
    