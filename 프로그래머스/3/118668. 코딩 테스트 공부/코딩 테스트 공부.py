# 각 문제에 필요한 alp, cop 을 하나의 노드로 생각하고, 다익스트라를 활용할 수 있다.
# 이 때 우선순위 큐를 활용하고, 기존 다익스트라의 distance 를 dp table 로 만든다.
import heapq

def solution(alp, cop, problems):
    
    # alp, cop 각각 1씩 늘리는 경우 추가
    problems = [[0,0,1,0,1], [0,0,0,1,1]] + problems
    dp = [[1e9] * 151 for _ in range(151)]
    
    max_alp = max(alp, max([p[0] for p in problems]))
    max_cop = max(cop, max([p[1] for p in problems]))
    
    queue = []
    # cost, alp, cop
    heapq.heappush(queue, (0, alp, cop))
    dp[alp][cop] = 0
    
    while queue:
        
        now_cost, now_alp, now_cop = heapq.heappop(queue)
        
        # 이 때 break 를 하게 되면, 우선순위큐 특징에 의해서 모든 문제를 풀 수 있으면서 가장 cost 가 낮다.
        if now_alp >= max_alp and now_cop >= max_cop:
            break
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            # 풀 수 있는 문제인 경우
            if now_alp >= alp_req and now_cop >= cop_req:
                
                # dp 테이블의 범주를 넘는 경우. 그 경우에는 최대범위를 갱신해주면 된다.
                new_alp = min(now_alp + alp_rwd, 150)
                new_cop = min(now_cop + cop_rwd, 150)
                
                if now_cost + cost < dp[new_alp][new_cop]:
                    dp[new_alp][new_cop] = now_cost + cost
                    heapq.heappush(queue, (now_cost + cost, new_alp, new_cop))
    
    # print(now_alp, now_cop)
    return dp[now_alp][now_cop]