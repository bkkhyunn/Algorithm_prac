import sys
input = sys.stdin.readline

nums = set([int(input()) % 42 for _ in range(10)])

print(len(nums))