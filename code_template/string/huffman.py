# Huffman Coding => 문서의 압축을 위해 문자들의 빈도수에 따라 코드 값을 부여한다.
# 출현 빈도가 낮은 문자부터 선택해서 이진 트리를 완성하고 코드 값을 부여한다.
# 허프만 알고리즘은 그리디 알고리즘을 이용해서 최적 코드에 해당하는 이진트리를 만들어 최적 이진 문자 코드를 만든다.
# 따라서 min-heap 이 이용된다.
# 허프만 알고리즘의 사용 이유는, 우리가 쓰는 문자를 컴퓨터 내에 저장할 때, 약속된 코드의 비트 수가 적을수록 메모리적으로 이득이다. 이를 통해 문서를 압축할 수 있다.

import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char # 노드에 해당하는 문자
        self.freq = freq # 해당 문자의 빈도수
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드
    
    # 우선순위 큐를 위해 x < y 를 판단하는 기준을 정의 (less than → lt)
    # 즉 우선순위 큐에서 사용할 비교 연산자로, 빈도수를 기준으로 비교
    def __lt__(self, other):
        return self.freq < other.freq

# frequency 는 주어진 문장의 빈도를 나타낸다.
def build_huffman_tree(frequency):
    '''
    허프만 트리 구성 작동 원리
    1. 빈도수를 기준으로 한 Priority Queue 에서 차례로 두 개를 선택
    2. 선택된 각각을 left와 right child에 배치하는 새로운 노드를 생성하여 binary subtree 생성
    3. 새로운 노드의 빈도수로서 선택된 두 빈도수의 합을 지정
    4. 그 새로운 노드를 Priority Queue에 삽입
    5. 2,3,4 의 과정을 반복하다가 Priority Queue 안에 값이 1개 뿐이면 종료.
    
    우선순위 큐
    1. 더 낮은 빈도 수의 노드
    2. 새롭게 구성된 노드
    3. 더 낮은 알파벳의 노드
    '''
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    # 빈도수를 priority value 로 min-heap 으로 구성한다.
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # 새롭게 구성된 노드
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    # 결국 heap 에는 1개만 남게 되는데, 이 1개가 허프만 트리의 루트 노드가 된다.
    return heap[0]

def build_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

# 주어진 문장을 인코딩
def huffman_encoding(data):
    if not data:
        return '', {}
    
    frequency = Counter(data)
    huffman_tree = build_huffman_tree(frequency)
    codebook = build_codes(huffman_tree)
    encoded_data = ''.join(codebook[char] for char in data)
    
    return encoded_data, codebook

# 인코딩된 문장을 디코딩하여 원 문장으로 복원
def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ''
    decoded_data = []
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data.append(reverse_codebook[current_code])
            current_code = ''
    
    return ''.join(decoded_data)

# Example
if __name__ == "__main__":
    data = "Hello, Bkkhyunn's algorithm practice"
    encoded_data, codebook = huffman_encoding(data)
    print(f"Encoded Data: {encoded_data}")
    print(f"Codebook: {codebook}")
    
    decoded_data = huffman_decoding(encoded_data, codebook)
    print(f"Decoded Data: {decoded_data}")
    
    assert data == decoded_data
