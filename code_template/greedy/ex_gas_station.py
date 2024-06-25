# 현재 도시의 주유 비용과 다음 도시의 주유 비용을 비교해서 주유 비용이 더 적으면 갱신하고, 더 크면 이전 주유 비용을 사용해서 총 주유량을 계산한다.
# 두 도시의 비용을 비교해서 더 적은 주유 비용을 선택하기 때문에 그리디 라고 할 수 있다.

import sys
from collections import deque

n = int(input())
dist = deque(list(map(int,sys.stdin.readline().split())))
cost = deque(list(map(int,sys.stdin.readline().split())))

now_cost = cost.popleft()
now_dist = dist.popleft()
total_cost = now_cost * now_dist

while dist:
    next_cost = cost.popleft()
    if now_cost > next_cost:
        now_cost = next_cost
        
    now_dist = dist.popleft()
    total_cost += now_dist * now_cost

print(total_cost)