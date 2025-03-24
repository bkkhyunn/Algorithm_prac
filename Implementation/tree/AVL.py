'''
- AVL 트리는 높이 균형(height balanced) 트리이며, 모든 노드의 왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이 간의 차이는 1이하 여야 한다.
- AVL 트리의 탐색 과정은 이진 탐색 트리의 탐색 방법과 동일하다. 또한 중위 순회를 하면 이진 탐색 트리처럼 정렬된 결과를 반환한다.
- AVL 트리에서 노드를 삽입하거나 삭제하면 균형이 깨질 수 있기 때문에 노드의 위치를 재구성하는 과정이 필요하다. 이 과정은 보통 노드를 회전(rotation)시키는 방법으로 구현된다. 회전은 부모와 자식 노드의 위치를 서로 바꾸는 연산이다.
- 불균형은 모두 4가지 유형(Left-Left, Right-Right, Left-Right, Right-Left)으로 나뉘는데, 이에 대응하는 회전 작업을 수행하는 식으로 균형을 맞춘다.
- AVL 트리는 레드-블랙 트리보다 더 엄격하게 균형을 유지하기 때문에 일반적으로 레드-블랙 트리보다 탐색은 빠르지만 삽입과 제거는 느리다.
'''

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:  # Left Heavy
            if self._balance_factor(node.left) < 0:  # Left Right Case
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)  # Left Left Case
        if balance < -1:  # Right Heavy
            if self._balance_factor(node.right) > 0:  # Right Left Case
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)  # Right Right Case

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # 중복된 키는 허용하지 않음

        return self._rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return self._rebalance(root)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

# 테스트
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(5)
avl_tree.insert(15)
avl_tree.insert(3)
avl_tree.insert(7)
avl_tree.insert(12)
avl_tree.insert(17)

print("Inorder Traversal:", avl_tree.inorder_traversal())  # 중위 순회 출력
avl_tree.delete(5)
print("After deleting 5:", avl_tree.inorder_traversal())  # 삭제 후 중위 순회 출력
