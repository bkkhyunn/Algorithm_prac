'''
- Node 클래스: 링크드 리스트의 각 노드를 나타낸다. 각 노드는 키, 값, 그리고 다음 노드에 대한 참조를 가진다.
- HashTable 클래스: 해시 테이블을 구현. 체이닝을 사용하여 각 인덱스에 링크드 리스트를 저장한다.
- 해시 함수: 키를 해시 값으로 변환하여 인덱스를 얻는다.
- 삽입: 주어진 키-값 쌍을 해시 테이블에 삽입한다. 충돌이 발생하면 링크드 리스트에 노드를 추가한다.
- 검색: 주어진 키에 해당하는 값을 해시 테이블에서 검색한다.
- 삭제: 주어진 키에 해당하는 값을 해시 테이블에서 삭제한다.
- 출력: 해시 테이블의 현재 상태를 출력한다.
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        """
        해시 함수: 키를 인덱스로 변환
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        해시 테이블에 키-값 쌍을 삽입
        """
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value  # 키가 이미 존재하면 값을 업데이트
                    return
                current = current.next
            if current.key == key:
                current.value = value  # 키가 이미 존재하면 값을 업데이트
            else:
                current.next = Node(key, value)

    def get(self, key):
        """
        해시 테이블에서 키에 해당하는 값을 반환
        """
        index = self._hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("해당 키가 존재하지 않습니다.")

    def delete(self, key):
        """
        해시 테이블에서 키에 해당하는 값을 삭제
        """
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        raise KeyError("해당 키가 존재하지 않습니다.")

    def __repr__(self):
        result = []
        for i, node in enumerate(self.table):
            chain = []
            current = node
            while current is not None:
                chain.append(f"{current.key}: {current.value}")
                current = current.next
            result.append(f"Index {i}: " + " -> ".join(chain))
        return "\n".join(result)

# 테스트
hash_table = HashTable()

# 삽입
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)
hash_table.insert("grape", 4)
hash_table.insert("peach", 5)
print("해시 테이블:\n", hash_table)

# 검색
print("apple:", hash_table.get("apple"))
print("banana:", hash_table.get("banana"))

# 삭제
hash_table.delete("banana")
print("해시 테이블 (after deletion):\n", hash_table)

# 존재하지 않는 키 검색
try:
    print(hash_table.get("banana"))
except KeyError as e:
    print(e)
