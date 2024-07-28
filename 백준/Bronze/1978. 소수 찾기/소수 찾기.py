import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
prime = 0
for i in range(n):
    if nums[i] != 1 and is_prime_number(nums[i]):
        prime += 1
print(prime)