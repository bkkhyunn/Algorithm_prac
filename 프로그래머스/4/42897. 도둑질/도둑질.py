# 점화식
# 각 탐색에서 자기 자신을 포함할 것인지, 아닌지에 따라 나눌 수 있다.
# DP[now] = max( DP[now-1] , DP[now-2] + DP[now] )

def solution(money):
    answer = 0
    dp_1 = [0] * len(money)
    dp_2 = [0] * len(money)
    
    if len(money) == 3:
        return money[0]
        
    for i, m in enumerate(money[:-1]):
        if i == 0:
            dp_1[i] = m
        
        elif i == 1:
            dp_1[i] = max(dp_1[i-1], m)
            
        else:
            dp_1[i] = max(dp_1[i-1], dp_1[i-2]+m)
            
    for i, m in enumerate(money[1:]):
        if i == 0:
            dp_2[i] = m
        
        elif i == 1:
            dp_2[i] = max(dp_2[i-1], m)
            
        else:
            dp_2[i] = max(dp_2[i-1], dp_2[i-2]+m)
            
    answer = max(dp_1[-2], dp_2[-2])
            
    return answer