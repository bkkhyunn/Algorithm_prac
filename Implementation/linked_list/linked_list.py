'''
Node
    - data는 노드의 데이터를 저장
    - next는 다음 노드를 가리킨다.
LinkedList
    - __init__: 초기화 메서드로, 빈 리스트를 생성
    - add: 리스트 끝에 노드를 추가
    - delete: 주어진 데이터를 가진 노드를 삭제
    - find: 주어진 데이터를 가진 노드를 찾는다.
    - print_list: 리스트의 모든 노드를 출력한다.
    - size: 리스트의 길이를 반환
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def delete(self, data):
        node = self.head
        if not node:
            return

        if node.data == data:
            self.head = node.next
            del node
            return

        prev_node = None
        while node:
            if node.data == data:
                prev_node.next = node.next
                del node
                return
            prev_node = node
            node = node.next

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print("None")

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

# 테스트
linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

linked_list.print_list()  # 출력: 1 -> 2 -> 3 -> None

linked_list.delete(2)
linked_list.print_list()  # 출력: 1 -> 3 -> None

print(linked_list.find(1))  # 출력: <__main__.Node object at ...>
print(linked_list.find(4))  # 출력: None

print("Size:", linked_list.size())  # 출력: Size: 2
