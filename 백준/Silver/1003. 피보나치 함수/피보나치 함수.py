t = int(input())

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
zero = [0] * 100
one = [0] * 100

# 재귀함수로 피보나치 함수 구현(Top down DP)
def fibo_zero(x):
    
    # 종료 조건
    if x == 0:
        zero[x] = 1
        return 1
    
    if x == 1:
        return 0
	  
    # 이미 계산한 적 있는 문제라면 그대로 반환. DP table 의 값을 확인한다.
    if zero[x] != 0:
        return zero[x]
	  
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    zero[x] = fibo_zero(x-1) + fibo_zero(x-2)
	  
    return zero[x]

# 재귀함수로 피보나치 함수 구현(Top down DP)
def fibo_one(x):
    
    # 종료 조건
    if x == 0:
        return 0
    if x == 1:
        one[x] = 1
        return 1
	  
    # 이미 계산한 적 있는 문제라면 그대로 반환. DP table 의 값을 확인한다.
    if one[x] != 0:
        return one[x]
	  
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    one[x] = fibo_one(x-1) + fibo_one(x-2)
	  
    return one[x]

for _ in range(t):
    x = int(input())
    z = fibo_zero(x)
    o = fibo_one(x)
    print(str(z)+' '+str(o))