'''
- 레드-블랙 트리는 자가 균형 이진 탐색 트리의 일종으로, 모든 노드를 레드 또는 블랙으로 표시하여 트리의 균형을 유지하기 때문에 레드-블랙 트리라고 부른다.
- 레드-블랙 트리는 구현이 복잡하지만 매우 효율적인 알고리즘이기 때문에 다양하게 활용된다.
- 각종 프로그래밍 언어의 연관 배열 자료형(파이썬의 딕셔너리, C++의 map이나 set 등)들은 대부분 레드-블랙 트리 기반으로 구현되어 있다.
- 레드-블랙 트리는 다음과 같은 규칙을 이용하여 균형을 유지한다.
    1. 모든 노드는 레드 또는 블랙이다.
    2. 뿌리 노드와 잎 노드는 블랙이다.
    3. 레드 노드의 자식 노드는 레드일 수 없고, 모두 블랙이어야 한다. 블랙 노드는 레드와 블랙 모두 자식 노드로 가질 수 있다.
    4. 뿌리 노드와 모든 잎 노드 사이에 있는 블랙 노드의 수는 모두 동일하다.
- 레드-블랙 트리의 규칙을 지키기 위해서, 모든 잎 노드는 아무 데이터도 갖지 않으면서 블랙인 NIL 노드가 된다. 이러한 노드를 센티넬(sentinel) 노드라고 부른다.
- 레드-블랙 트리의 탐색 과정은 이진 탐색 트리의 탐색 방법과 동일하다.
- 레드-블랙 트리에서 노드를 삽입하거나 삭제하면 균형이 깨질 수 있기 때문에 노드의 색을 바꾸거나 노드를 회전하는 과정이 필요하다. 회전은 방향에 따라 좌회전과 우회전으로 구분된다.
'''

class TreeNode:
    def __init__(self, key, color="RED"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # 노드의 색상 (RED 또는 BLACK)

class RedBlackTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, node):
        """
        왼쪽으로 회전
        """
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        """
        오른쪽으로 회전
        """
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def _fix_insertion(self, node):
        """
        레드-블랙 트리 속성 유지를 위한 삽입 후 수정
        """
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_left(node.parent.parent)
        self.root.color = "BLACK"

    def insert(self, key):
        """
        삽입 연산
        """
        new_node = TreeNode(key)
        parent = None
        current = self.root

        # 이진 탐색 트리의 삽입
        while current:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self._fix_insertion(new_node)

    def inorder_traversal(self):
        """
        중위 순회
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

# 테스트
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(5)
rb_tree.insert(15)
rb_tree.insert(3)
rb_tree.insert(7)
rb_tree.insert(12)
rb_tree.insert(17)

print("Inorder Traversal:", rb_tree.inorder_traversal())  # 중위 순회 출력
