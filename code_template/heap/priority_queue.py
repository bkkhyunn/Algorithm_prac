'''
- 힙은 완전 이진 트리 자료구조의 일종이다.
- 힙에서는 항상 루트 노드를 제거한다.
- 최소 힙(min heap)
    - 루트 노드가 가장 작은 값을 가진다.
    - 따라서 값이 작은 데이터가 우선적으로 제거된다.
- 최대 힙(max heap)
    - 루트 노드가 가장 큰 값을 가진다.
    - 따라서 값이 큰 데이터가 우선적으로 제거된다.
- 완전 이진 트리
    - 힙은 완전 이진 트리를 따른다.
    - 완전 이진 트리란 루트 노드부터 시작하여 왼쪽 자식노드, 오른쪽 자식노드 순서대로 데이터가 차례대로 삽입되는 트리를 의미한다.
'''

import heapq

def heapsort_asc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def heapsort_desc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result