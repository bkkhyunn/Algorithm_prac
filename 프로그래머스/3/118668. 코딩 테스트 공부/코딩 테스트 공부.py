# 각 문제에 필요한 alp, cop 을 하나의 노드로 생각하고, 다익스트라를 활용할 수 있다.
# 이 때 우선순위 큐를 활용하고, 기존 다익스트라의 distance 를 dp table 로 만든다.
import heapq

def solution(alp, cop, problems):
    
    # alp, cop 각각 1씩 늘리는 경우 추가
    problems = [[0,0,1,0,1], [0,0,0,1,1]] + problems
    dp = [[1e9] * 151 for _ in range(151)]
    
    # 기존의 alp, cop 으로 모든 문제를 푸는 경우가 있을 수 있다.
    max_alp = max(alp, max([p[0] for p in problems]))
    max_cop = max(cop, max([p[1] for p in problems]))
    
    queue = []
    # cost, alp, cop
    heapq.heappush(queue, (0, alp, cop))
    dp[alp][cop] = 0
    
    while queue:
        
        now_cost, now_alp, now_cop = heapq.heappop(queue)
        
        # 이 때 break 를 하게 되면, 우선순위큐 특징에 의해서 dp[now_alp][now_cop]으로
        # 모든 문제를 풀 수 있으면서 가장 낮은 cost 를 얻을 수 있다.
        if now_alp >= max_alp and now_cop >= max_cop:
            break
            
        if dp[now_alp][now_cop] < now_cost:
            continue
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            
            # 풀 수 있는 문제인 경우
            if now_alp >= alp_req and now_cop >= cop_req:
                
                # 예를 들어 max_alp, max_cop 이 150, 150 인 경우
                # 문제를 하나 풀어 new_alp, new_cop 이 151, 154 같이 될 수 있다.
                # 그 경우에는 최대범위(150, 150)를 갱신해주면 된다.
                new_alp = min(now_alp + alp_rwd, 150)
                new_cop = min(now_cop + cop_rwd, 150)
                
                if now_cost + cost < dp[new_alp][new_cop]:
                    dp[new_alp][new_cop] = now_cost + cost
                    heapq.heappush(queue, (now_cost + cost, new_alp, new_cop))
    
    # print(now_alp, now_cop)
    return dp[now_alp][now_cop]