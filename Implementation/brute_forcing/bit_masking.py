## 비트마스킹 집합의 연산
S = 0b000000000000
n = 3

# 3번째에 원소 추가
S |= (1 << n)

# 원소 삭제
S &= ~(1 << n)

# 원소 토글 : S 에 n 이 있다면 삭제, 없다면 추가하는 연산
S ^= (1 << n)

# 원소 체크
print(1 if S & (1 << n) else 0)

# 원소 비우기 및 채우기
S = 0 # 비우기(공집합)
S = (1 << (len(S) + 1)) - 1 # 채우기

# 비트 연산자를 활용한 집합 연산
A = {1,2,3}
B = {2,3,4}

A | B # 합집합
A & B # 교집합
A & ~B # 차집합
A ^ B # A 와 B 중 하나에만 포함된 원소들의 집합

# ~ 연산 : 파이썬에서는 무한 비트이므로 그냥 비트 반전을 이용하면 모든 비트를 반전시켜 2의 보수 표현이 사용된다.
def invert_bits(n, bit_length):
    mask = (1 << bit_length) - 1  # 예를 들어 4비트면 0b1111
    return ~n & mask

# 4비트로 반전
n = 0b1010
bit_length = 4
inverted = invert_bits(n, bit_length)
print(bin(inverted))  # 0b0101

# 집합의 크기
# x % 2 는 비트의 맨 마지막 원소, x // 2 는 비트의 맨 마지막 원소 삭제
def bit_count(x):
    if x == 0:
        return 0
    return x % 2 + bit_count(x//2)

# 모든 부분집합 순회
def generate_subsets(elements):
    n = len(elements)
    subsets = []
    
    # 총 2^n개의 부분집합을 생성. -> 비트열은 n+1 개가 생긴다.
    for i in range(1 << n):
        subset = []
        for j in range(n):
            # i의 j번째 비트가 1인지 확인
            if i & (1 << j):
                subset.append(elements[j])
        subsets.append(subset)
    
    return subsets

# 예시 테스트
elements = ['a', 'b', 'c']
all_subsets = generate_subsets(elements)
for subset in all_subsets:
    print(subset)

# Output:
# []
# ['a']
# ['b']
# ['a', 'b']
# ['c']
# ['a', 'c']
# ['b', 'c']
# ['a', 'b', 'c']