# 가장 오른쪽에 있는 1 비트를 찾아낸다.

def rightmost_set_bit(x):
    '''
    1. 2의 보수를 사용하여 -x 를 계산한다.
       - 18의 이진 표현: 0001 0010
       - 18의 1의 보수: 1110 1101 (모든 비트를 반전)
       - 18의 2의 보수 (즉, -18): 1110 1110 (1의 보수에 1을 더함)
    2. x 와 -x 의 AND 연산을 한다.
    '''
    return x & -x

# Example usage
print(bin(rightmost_set_bit(18)))  # Output: 0b10 (binary 10010)