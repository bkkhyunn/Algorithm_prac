# Binary Search Tree
# 이진 탐색 트리란 이진 탐색을 위해서 구성하는 이진 트리로, 왼쪽 자식 노드는 부모 노드보다 작고 오른쪽 자식 노드는 부모 노드보다 크다는 규칙을 따른다.
# 이진 탐색 트리를 중위 순회(inorder traversal)하면, 모든 노드를 정렬된 순서로 탐색한다.
# 이진 탐색 트리는 이진 탐색이 가능한 상태로 정렬되어 있어야 한다. 이러한 상태를 유지하려면 노드의 삽입과 삭제가 이루어질 때마다 별도의 작업을 수행해야 한다.
# 이진 탐색 트리에서 노드의 삽입 연산은 이진 탐색으로 새 노드를 연결할 부모 노드를 찾아낸 후 그곳에 연결하는 방식으로 이루어진다. 삽입할 노드는 항상 트리의 잎 노드로 삽입된다.
# 이진 탐색 트리에서 노드의 삭제 연산은 일단 이진 탐색으로 삭제할 노드의 위치를 찾고, 그 노드를 트리에서 떼어내는 작업이 필요하다. 이때 삭제할 노드의 위치에 따라 수행 과정이 달라진다.

class TreeNode:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

class BST:
    def __init__(self):
        self.root = None  # 이진 탐색 트리의 루트 노드

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # 삽입할 위치를 찾아 삽입
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        # 트리에서 키를 검색
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # 키를 삭제하고 새로운 루트 노드를 반환
        if node is None:
            return node

        # 삭제할 노드 찾기
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # 자식이 없거나 하나만 있는 경우
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 두 자식이 모두 있는 경우
            # 오른쪽 서브트리에서 최솟값을 찾아 현재 노드의 값을 갱신
            node.key = self._min_value(node.right)
            # 오른쪽 서브트리에서 최솟값을 삭제
            node.right = self._delete(node.right, node.key)

        return node

    def _min_value(self, node):
        # 가장 작은 값을 가진 노드 찾기
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def inorder_traversal(self):
        # 중위 순회
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        # 전위 순회
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        # 후위 순회
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.key)

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder Traversal:", bst.inorder_traversal())  # 중위 순회 출력
print("Preorder Traversal:", bst.preorder_traversal())  # 전위 순회 출력
print("Postorder Traversal:", bst.postorder_traversal())  # 후위 순회 출력
