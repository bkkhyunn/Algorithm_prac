import math

n = 1000 # 2 부터 1,000 까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True) 인 것으로 초기화(0과 1은 제외)
# 이제 각각의 수가 소수인지 아닌지에 대한 내용은 array 테이블의 인덱스에 접근해서 확인 가능.
array = [True for i in range(n+1)]

# 에라토스테네스의 체
# 2 부터 n의 제곱근까지 모든 수를 확인
for i in range(2, int(math.sqrt(n))+1):
    # i 가 소수인 경우(남은 수인 경우)
    if array[i] == True:
        # i 를 제외한 i 의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end= ' ')