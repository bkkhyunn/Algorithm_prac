import sys
input = sys.stdin.readline

n = input()
nums = list(map(int, input().split()))

print(f"{min(nums)} {max(nums)}")