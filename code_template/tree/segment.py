'''
- 어떤 데이터가 존재할 때, 특정 구간의 결과값을 구하는데 사용하는 자료구조이다.
- 단순한 구간합 뿐만 아니라주어진 쿼리에 대해 빠르게 응답하기 위한 자료구조이기도 하다.
- 세그먼트 트리는 이진트리를 기본으로 한다.
'''

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)  # 세그먼트 트리를 저장할 배열
        self.build(nums, 1, 0, self.n - 1)

    def build(self, nums, idx, left, right):
        if left == right:
            self.tree[idx] = nums[left]
        else:
            mid = (left + right) // 2
            self.build(nums, 2 * idx, left, mid)
            self.build(nums, 2 * idx + 1, mid + 1, right)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def update(self, idx, val):
        """
        세그먼트 트리의 idx번째 값을 val로 업데이트하는 메서드
        """
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, tree_idx, left, right, idx, val):
        if left == right == idx:
            self.tree[tree_idx] = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self._update(2 * tree_idx, left, mid, idx, val)
        else:
            self._update(2 * tree_idx + 1, mid + 1, right, idx, val)
        self.tree[tree_idx] = self.tree[2 * tree_idx] + self.tree[2 * tree_idx + 1]

    def query(self, ql, qr):
        """
        세그먼트 트리에서 구간 [ql, qr]의 합을 반환하는 메서드
        """
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, idx, left, right, ql, qr):
        if qr < left or right < ql:  # 현재 노드가 구간에 완전히 벗어날 경우
            return 0
        elif ql <= left and right <= qr:  # 현재 노드가 구간에 완전히 포함될 경우
            return self.tree[idx]
        else:
            mid = (left + right) // 2
            return self._query(2 * idx, left, mid, ql, qr) + self._query(2 * idx + 1, mid + 1, right, ql, qr)

# 테스트
nums = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(nums)

print("Original Array:", nums)
print("Segment Tree:", seg_tree.tree)

print("Query [1, 3]:", seg_tree.query(1, 3))
seg_tree.update(2, 6)
print("After Update [2, 6]:", seg_tree.tree)
