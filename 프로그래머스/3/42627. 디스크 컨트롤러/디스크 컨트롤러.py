import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort()
    s_req, s_duration = heapq.heappop(jobs)
    wait_list = [[s_duration, s_req]]
    now_time, wait_time = 0, 0

    while wait_list:
        #print(wait_list)
        duration, req = heapq.heappop(wait_list)
        if req > now_time:
            wait_time = 0
            now_time += (req - now_time + duration)
        else:
            wait_time = (now_time - req)
            now_time += duration
        #print(now_time, wait_time)
        answer += (wait_time + duration)
        #print(answer)
        
        while jobs and (jobs[0][0] < now_time):
            n_req, n_duration = heapq.heappop(jobs)
            heapq.heappush(wait_list, [n_duration, n_req])
            
        if jobs and (not wait_list):
            n_req, n_duration = heapq.heappop(jobs)
            wait_list += [[n_duration, n_req]]
    
    return int(answer / n)