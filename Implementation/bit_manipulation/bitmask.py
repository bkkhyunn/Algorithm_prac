# 주어진 길이만큼 bit mask 만들기

def bitmask(bit_length):
    return (1 << bit_length) - 1

# Example usage
print(bin(bitmask(5)))  # Output: 0b11111