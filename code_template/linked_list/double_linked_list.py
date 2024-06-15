'''
- 더블 링크드 리스트를 구현하면 각 노드에서 바로 이전 노드와 다음 노드로 이동할 수 있어, 노드의 삽입이나 삭제 등의 연산이 더 유연해진다.
- 단일 링크드 리스트에서 노드를 삭제하려면 삭제하려는 노드의 이전 노드를 알아야 한다. 이전 노드의 next 포인터를 삭제하려는 노드의 다음 노드로 설정하기 때문이다.
- 그러나 더블 링크드 리스트에서는 각 노드가 이전 노드에 대한 포인터(prev)도 가지므로, 이전 노드를 쉽게 알 수 있어 삭제 연산이 좀 더 간단해지는 것이다.

- 차이점
    - 포인터 수: 링크드 리스트는 하나의 포인터(next)를 가지는 반면, 더블 링크드 리스트는 두 개의 포인터(next와 prev)를 가진다.
    - 연결 방향: 링크드 리스트는 단방향으로 연결되고, 더블 링크드 리스트는 양방향으로 연결된다.
    - 순회: 링크드 리스트는 한 방향으로만 순회할 수 있지만, 더블 링크드 리스트는 양방향으로 순회할 수 있다.
    - 삽입 및 삭제: 더블 링크드 리스트는 삽입 및 삭제가 더 유연하며, 노드 삭제 시 이전 노드를 몰라도 된다.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            new_node.prev = node

    def delete(self, data):
        node = self.head
        while node:
            if node.data == data:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if node == self.head:
                    self.head = node.next
                del node
                return
            node = node.next
        raise KeyError("해당 데이터가 존재하지 않습니다.")

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def print_list_forward(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print("None")

    def print_list_backward(self):
        node = self.head
        if not node:
            print("None")
            return
        while node.next:
            node = node.next
        while node:
            print(node.data, end=" -> ")
            node = node.prev
        print("None")

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

# 테스트
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add(1)
doubly_linked_list.add(2)
doubly_linked_list.add(3)

print("Forward:")
doubly_linked_list.print_list_forward()  # 출력: 1 -> 2 -> 3 -> None

print("Backward:")
doubly_linked_list.print_list_backward()  # 출력: 3 -> 2 -> 1 -> None

doubly_linked_list.delete(2)
print("After deletion (Forward):")
doubly_linked_list.print_list_forward()  # 출력: 1 -> 3 -> None

print("Size:", doubly_linked_list.size())  # 출력: Size: 2
