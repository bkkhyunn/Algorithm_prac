def swap(a, b):
    '''
    a ^= b: a는 a와 b의 XOR 결과를 가짐.
    b ^= a: b는 b와 새로운 a의 XOR 결과, 즉 원래 a의 값을 가짐.
    a ^= b: a는 새로운 b와 새로운 a의 XOR 결과, 즉 원래 b의 값을 가짐.
    '''
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Example usage
a, b = 5, 9
a, b = swap(a, b)
print(a, b)  # Output: 9 5
