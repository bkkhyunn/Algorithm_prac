# Brian Kernighan's Algorithm
# 이진수 비트 중 가장 오른쪽에 위치한 1을 제거하기 위해서는 n = n & (n-1)을 사용한다.
# 이렇게 while 문을 돌게 되면 모든 1이 제거된 후 n이 0이 되었을 때 while 문이 끝나게 되고, count 값은 1이 제거될 때마다 1씩 추가되어서 결과값이 된다.
def count_bits_kernighan(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count