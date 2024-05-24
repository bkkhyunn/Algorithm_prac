import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    
    # jobs 를 요청시점이 빠른 순대로 정렬하고 가장 빨리 요청된 작업을 wait_list 에 넣어준다.
    jobs.sort()
    s_req, s_duration = heapq.heappop(jobs)
    
    # wait_list 는 대기열로, 진행 중인 작업이 끝나는 시점보다 빨리 요청된 작업들이 들어간다.
    # 이 때, 소요시간이 빠른 순대로 삽입한다. 소요시간이 빠른 작업부터 진행해야 총 평균 시간이 작아지기 때문이다.
    wait_list = [[s_duration, s_req]]
    now_time, wait_time = 0, 0

    while wait_list:
        #print(wait_list)
        duration, req = heapq.heappop(wait_list)
        
        # 요청시점이 현재 시간보다 크면, 대기하지 않는다.
        if req > now_time:
            wait_time = 0
            now_time += (req - now_time + duration)
        # 반대의 경우 대기 시간이 생긴다.
        else:
            wait_time = (now_time - req)
            now_time += duration
        #print(now_time, wait_time)
        answer += (wait_time + duration)
        #print(answer)
        
        # 현재 시간(진행 중인 작업이 끝나는 시간) 보다 더 빨리 요청된 작업들을 wait_list 에 min heap 형태로 삽입한다.
        while jobs and (jobs[0][0] < now_time):
            n_req, n_duration = heapq.heappop(jobs)
            heapq.heappush(wait_list, [n_duration, n_req])
            
        # 하드디스크가 작업을 안하는 시점이 생길 수 있는데, 이를 위해 wait_list 가 비었고 남은 작업이 있을 때 요청시점이 제일 빠른 작업을 넣는다.
        if jobs and (not wait_list):
            n_req, n_duration = heapq.heappop(jobs)
            wait_list += [[n_duration, n_req]]
    
    return int(answer / n)