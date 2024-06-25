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