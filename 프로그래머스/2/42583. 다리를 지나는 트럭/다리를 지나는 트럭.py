from collections import deque

# 위 코드에서 대기 트럭이 없어지는 경우, 다리에 마지막 트럭이 올라간 바로 직후이기 때문에
# 거기서 멈춰서 다리 길이 만큼 총 시간에 더해주면 더 쉬워진다.
def solution(bridge_length, weight, truck_weights):
    total_time = 0
    
    wait_truck = deque(truck_weights)
    on_bridge = deque([])
    on_bridge_w = 0
    
    while wait_truck:
        
        total_time += 1
        
        if on_bridge_w + wait_truck[0] <= weight:
            w = wait_truck.popleft()
            on_bridge.appendleft(w)
            on_bridge_w += w

        else:
            on_bridge.appendleft(0)

        if len(on_bridge) == bridge_length:
            w = on_bridge.pop()
            on_bridge_w -= w
            
    total_time += bridge_length
    
    return total_time