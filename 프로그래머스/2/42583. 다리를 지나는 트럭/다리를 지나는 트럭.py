from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_time = 0
    
    wait_truck = deque(truck_weights)
    on_bridge = deque([])
    arrive_truck = []
    on_bridge_w = 0
    
    while len(arrive_truck) != len(truck_weights):
        
        if wait_truck:
            if on_bridge_w + wait_truck[0] <= weight:
                w = wait_truck.popleft()
                on_bridge.appendleft(w)
                on_bridge_w += w
                total_time += 1

            else:
                on_bridge.appendleft(0)
                total_time += 1
            
            #print(total_time, on_bridge)
                
            if len(on_bridge) == bridge_length:
                w = on_bridge.pop()
                on_bridge_w -= w
                
                if w > 0:
                    arrive_truck.append(w)
        else:
            while sum(on_bridge) != 0:
                
                if len(on_bridge) == bridge_length:
                    on_bridge.appendleft(0)
                    total_time += 1
                    w = on_bridge.pop()

                    if w > 0:
                        arrive_truck.append(w)
                
                else:
                    on_bridge.appendleft(0)
                    total_time += 1
                #print(total_time, on_bridge)
    
    return total_time