class SegmentTree:
    '''
    SegmentTree

    build : 주어진 배열을 기반으로 세그먼트 트리를 구성
    query : 주어진 범위 내에서 최소값을 찾는다.
    '''
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_query = self._query(2 * node + 1, start, mid, l, r)
        right_query = self._query(2 * node + 2, mid + 1, end, l, r)
        return min(left_query, right_query)

class LCATree:
    '''
    LCATree 클래스:

    add_edge : 트리에 간선 추가
    dfs : 오일러 투어를 수행하면서, 각 노드를 방문한 순서와 깊이를 기록
    build : 오일러 투어(dfs)를 수행한 후, 깊이와 노드 정보를 기반으로 세그먼트 트리를 구성
    lca : 두 노드의 LCA 찾기
    '''
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.euler = []
        self.depth = []
        self.first = [-1] * n
        self.segment_tree = None

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, d):
        self.first[node] = len(self.euler)
        self.euler.append(node)
        self.depth.append(d)
        for neighbor in self.graph[node]:
            if self.first[neighbor] == -1:  # 아직 방문하지 않은 경우
                self.dfs(neighbor, d + 1)
                self.euler.append(node)
                self.depth.append(d)

    def build(self, root=0):
        self.dfs(root, 0)
        depth_pairs = [(self.depth[i], self.euler[i]) for i in range(len(self.depth))]
        self.segment_tree = SegmentTree(depth_pairs)

    def lca(self, u, v):
        if self.first[u] > self.first[v]:
            u, v = v, u
        l = self.first[u]
        r = self.first[v]
        _, lca_node = self.segment_tree.query(l, r)
        return lca_node

n = 7
tree = LCATree(n)
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]

for u, v in edges:
    tree.add_edge(u, v)

tree.build(0)  # 루트를 0으로 설정

print(tree.lca(3, 4))  # 출력: 1
print(tree.lca(3, 5))  # 출력: 0
print(tree.lca(4, 6))  # 출력: 0
print(tree.lca(2, 6))  # 출력: 2
