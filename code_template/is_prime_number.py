import math

# 소수 판별 함수 (2 이상의 자연수에 대하여)
def is_prime_number(x):
    # 2 부터 x 의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True	      