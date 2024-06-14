# 특정 위치의 비트를 1로 설정
def set_bit(x, pos):
    return x | (1 << pos)

# Example usage
print(bin(set_bit(5, 1)))  # Output: 0b111 (binary 101 -> 111)


# 특정 위치의 비트를 0으로 설정
def clear_bit(x, pos):
    return x & ~(1 << pos)

# Example usage
print(bin(clear_bit(5, 0)))  # Output: 0b100 (binary 101 -> 100)