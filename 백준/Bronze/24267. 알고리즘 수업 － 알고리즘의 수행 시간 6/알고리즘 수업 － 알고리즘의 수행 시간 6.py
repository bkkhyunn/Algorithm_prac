import sys

input = sys.stdin.read
n = int(input().strip())

if n < 3:
    print(0)
else:
    count = n * (n - 1) * (n - 2) // 6
    print(count)
    
print(3)