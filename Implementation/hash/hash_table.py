'''
- 해시 테이블(Hash Table)은 키-값 쌍을 저장하고, 키를 이용하여 값을 빠르게 검색할 수 있는 자료구조이다.
- 파이썬에서는 기본적으로 딕셔너리(dictionary)가 해시 테이블로 구현되어 있다. 그러나 어떤 방식으로 동작하는 건지 보자. 코딩테스트에서는 그냥 dict 를 쓰면 된다.
- 해시 함수: 키를 해시 값으로 변환하여 인덱스를 얻는다.
- 삽입: 주어진 키-값 쌍을 해시 테이블에 삽입한다. 이미 키가 존재하면 값을 업데이트하고, 충돌이 발생하면 선형 탐사를 사용하여 새로운 위치를 찾는다.
    - 충돌 해결 방법으로 개방 주소법(Open Addressing) 중 선형 탐사법(Linear Probing)을 사용한 것이다.
- 검색: 주어진 키에 해당하는 값을 해시 테이블에서 검색한다.
- 삭제: 주어진 키에 해당하는 값을 해시 테이블에서 삭제한다. 삭제 후, 테이블을 재정렬하여 공백을 제거한다.
- 재정렬: 삭제로 인한 공백을 제거하기 위해 테이블을 재정렬한다.
'''

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
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # 키가 이미 존재하면 값을 업데이트
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("해시 테이블이 가득 찼습니다.")
        self.table[index] = (key, value)

    def get(self, key):
        """
        해시 테이블에서 키에 해당하는 값을 반환
        """
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError("해당 키가 존재하지 않습니다.")

    def delete(self, key):
        """
        해시 테이블에서 키에 해당하는 값을 삭제
        """
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self._rehash()
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError("해당 키가 존재하지 않습니다.")

    def _rehash(self):
        """
        테이블을 재정렬하여 삭제된 키로 인한 공백을 제거
        """
        old_table = self.table[:]
        self.table = [None] * self.size
        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    def __repr__(self):
        return str(self.table)

# 테스트
hash_table = HashTable()

# 삽입
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)
print("해시 테이블:", hash_table)

# 검색
print("apple:", hash_table.get("apple"))
print("banana:", hash_table.get("banana"))

# 삭제
hash_table.delete("banana")
print("해시 테이블 (after deletion):", hash_table)

# 존재하지 않는 키 검색
try:
    print(hash_table.get("banana"))
except KeyError as e:
    print(e)
