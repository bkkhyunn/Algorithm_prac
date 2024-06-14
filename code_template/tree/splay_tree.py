'''
스플레이 트리는 자주 탐색되는 노드를 뿌리 노드에 가깝게 위치하도록 만드는 이진 탐색 트리이다.
스플레이 트리에서 탐색, 삽입, 삭제 연산이 일어날 때마다 특정 노드를 뿌리로 옮기는 연산이 필요한데, 이를 스플레잉(Splaying)이라 부른다.
스플레잉은 Zig, Zig-Zig, Zig-Zag의 세 가지 유형으로 나뉜다.
    x: 최근에 접근한 노드, p: x의 부모 노드, g: x의 조부모 노드
    Zig step: p가 트리의 뿌리 노드인 경우에 수행된다. p와 x의 간선 연결을 회전시킨다.
    Zig-Zig step: p가 루트가 아니고 x와 p가 동일하게 왼쪽 자식 또는 오른쪽 자식인 경우에 수행된다. p와 g와의 간선 연결을 회전시키고, 그다음에 x와 p의 간선 연결을 회전시킨다.
    Zig-Zag step: p가 루트가 아니고 x가 왼쪽 자식, p가 오른쪽 자식이거나 그 반대인 경우(x가 오른쪽 자식, p가 왼쪽 자식)에 수행된다. x와 p의 간선 연결을 회전시키고, 그다음에 x와 x의 새로운 부모 p와의 간선 연결을 회전시킨다.
스플레이 트리는 평균적인 상황에서 다른 이진 탐색 트리 알고리즘과 성능이 비슷하며 참조 지역성이 중요한 경우 유용한 알고리즘이다. 하지만 트리의 균형이 깨지기 쉽다는 단점도 있다.
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root and self.root.key == key

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        # 루트 노드로 키를 탐색하여 도달한 노드로 스플레이
        self.root = self._splay(self.root, key)

        # 삽입할 위치를 찾음
        if key < self.root.key:
            new_node = Node(key)
            new_node.left = self.root.left
            new_node.right = self.root
            self.root.left = None
            self.root = new_node
        elif key > self.root.key:
            new_node = Node(key)
            new_node.right = self.root.right
            new_node.left = self.root
            self.root.right = None
            self.root = new_node
        else:  # 이미 키가 존재하는 경우
            return

    def _splay(self, node, key):
        if not node or node.key == key:
            return node

        if key < node.key:
            if not node.left:
                return node
            if key < node.left.key:
                # Zig-Zig (왼쪽 자식의 왼쪽 자식)
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                # Zig-Zag (왼쪽 자식의 오른쪽 자식)
                node.left.right = self._splay(node.left.right, key)
                if node.left.right:
                    node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        else:
            if not node.right:
                return node
            if key > node.right.key:
                # Zig-Zig (오른쪽 자식의 오른쪽 자식)
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            elif key < node.right.key:
                # Zig-Zag (오른쪽 자식의 왼쪽 자식)
                node.right.left = self._splay(node.right.left, key)
                if node.right.left:
                    node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

# 테스트
splay_tree = SplayTree()
splay_tree.insert(10)
splay_tree.insert(5)
splay_tree.insert(15)
splay_tree.insert(20)

print("Search 5:", splay_tree.search(5))  # True
print("Search 10:", splay_tree.search(10))  # True
print("Search 15:", splay_tree.search(15))  # True
print("Search 20:", splay_tree.search(20))  # True
print("Search 25:", splay_tree.search(25))  # False