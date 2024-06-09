from collections import deque

def solution(priorities, location):
    
    priorities = [(priority, idx) for idx, priority in enumerate(priorities)]
    queue = deque(priorities)
    cnt = 0
    
    while queue:
        max_prior = max(queue, key=lambda x: x[0])[0]
        process = queue.popleft()
        
        if process[0] < max_prior:
            queue.append(process)
        
        else:
            # 실행
            cnt += 1
            
            if process[1] == location:
                return cnt