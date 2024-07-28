import math
n = int(input())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if n != 1:
    nums = []
    while not is_prime_number(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                nums.append(i)
                n //= i
                break
    
    nums.append(n)
    nums.sort()
    
    for n in nums:
        print(n)