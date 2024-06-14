def next_power_of_2(x):
    if x == 0:
        return 1
    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x + 1

# Example usage
print(next_power_of_2(5))  # Output: 8
print(next_power_of_2(17)) # Output: 32
