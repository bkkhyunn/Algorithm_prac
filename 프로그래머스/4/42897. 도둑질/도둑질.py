# 점화식
# 각 탐색에서 자기 자신을 포함할 것인지, 아닌지에 따라 나눌 수 있다.
# 자기 자신을 포함하는 경우와 포함하지 않는 경우를 비교한다.
# DP[now] = max( DP[now-1] , DP[now-2] + DP[now] )

# 원형 탐색의 특징과 문제 조건에 따라 맨 처음 집에 들어간 경우와 맨 처음 집을 넘기고 다음 집부터 들어간 경우로 나눠 생각한다.

def solution(money):
    answer = 0
    dp_1 = [0] * len(money)
    dp_2 = [0] * len(money)
    
    # 3개 집 밖에 없을 때는 최대값
    if len(money) == 3:
        return max(money)
        
    # 맨 처음 집에 들어간 경우 -> 맨 마지막 집을 고려하지 않는다.
    for i, m in enumerate(money[:-1]):
        if i == 0:
            dp_1[i] = m
        
        elif i == 1:
            dp_1[i] = max(dp_1[i-1], m)
            
        else:
            dp_1[i] = max(dp_1[i-1], dp_1[i-2]+m)
            
    # 두번째 집부터 들어간 경우 -> 맨 마지막 집을 고려한다.
    for i, m in enumerate(money[1:]):
        if i == 0:
            dp_2[i] = m
        
        elif i == 1:
            dp_2[i] = max(dp_2[i-1], m)
            
        else:
            dp_2[i] = max(dp_2[i-1], dp_2[i-2]+m)
            
    answer = max(dp_1[-2], dp_2[-2])
            
    return answer