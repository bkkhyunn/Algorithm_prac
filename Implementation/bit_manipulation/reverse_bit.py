# ~ 연산 : 파이썬에서는 무한 비트이므로 그냥 비트 반전을 이용하면 모든 비트를 반전시켜 2의 보수 표현이 사용된다.

def reverse_bits(x, bit_size=32):
    result = 0
    for _ in range(bit_size):
        result = (result << 1) | (x & 1)
        x >>= 1
    return result

# Example usage
print(bin(reverse_bits(3, 4)))  # Output: 0b1100 (binary 0011 reversed to 1100)
