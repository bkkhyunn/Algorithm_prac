import math
n = int(input())
m = int(input())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

min_prime = 1e9
sum_prime = 0
for num in range(n, m+1):
    if num != 1 and is_prime_number(num):
        min_prime = min(min_prime, num)
        sum_prime += num
        
if sum_prime:
    print(sum_prime)
    print(min_prime)
else:
    print(-1)