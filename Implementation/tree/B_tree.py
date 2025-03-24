'''
- B-트리는 정렬된 데이터를 유지하면서 검색, 조회, 삽입, 삭제 연산을 로그 시간 내에 할 수 있는 자가 균형 트리이다. B-트리는 데이터베이스, 파일 시스템 등의 다양한 분야에 활용된다.
- B-트리의 특징은 다음과 같다. 여기서 t는 자연수 상수이다.
    1. 루트 노드는 1개 이상 2t개 미만의 오름차순으로 정렬된 키를 갖는다.
    2. 루트 노드가 아닌 모든 노드는 (t-1)개 이상 2t개 미만의 오름차순으로 정렬된 키를 갖는다.
    3. 내부 노드는 자신이 가진 키의 개수보다 하나 더 많은 자식을 갖는다.
    4. 각 노드의 한 키의 왼쪽 서브트리에 있는 모든 키값은 그 키값보다 작다. 각 노드의 한 키의 오른쪽 서브트리에 있는 모든 키값은 그 키값보다 크다.
    5. 모든 잎 노드의 레벨은 동일하다.
'''

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            # 리프 노드에 직접 삽입
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # 적절한 자식 노드로 이동
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)
        parent.children.insert(index + 1, new_child)
        parent.keys.insert(index, child.keys[t - 1])
        new_child.keys = child.keys[t:(2 * t - 1)]
        child.keys = child.keys[0:(t - 1)]
        if not child.leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[0:(t - 1)]

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self._search(node.children[i], key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            i = 0
            while i < len(node.keys):
                if not node.leaf:
                    self._inorder_traversal(node.children[i], result)
                result.append(node.keys[i])
                i += 1
            if not node.leaf:
                self._inorder_traversal(node.children[i], result)

# 테스트
b_tree = BTree(t=3)
keys = [10, 5, 15, 3, 7, 12, 17]
for key in keys:
    b_tree.insert(key)

print("Inorder Traversal:", b_tree.inorder_traversal())  # 중위 순회 출력
