import heapq, math
from collections import deque

def solution(jobs):
    answer = []
    
    queue, working = [], deque([])
    jobs = [(duration, request, i) for i, (request, duration) in enumerate(jobs)]
    jobs = deque(sorted(jobs, key=lambda x: x[1]))
    
    time = 0
    while True:
        
        # 종료 조건
        if (len(jobs) == 0) and (len(queue) == 0) and (len(working) == 0):
            break
        
        # jobs 내 요청시간이 됐으면 대기 큐에 적재
        while jobs and (jobs[0][1] <= time):
            job = jobs.popleft()
            heapq.heappush(queue, job)
        
        # 대기 중인 작업이 있을 때
        if queue:
            # 디스크가 작업 중
            if working:
                # 작업이 끝날 시점이면 꺼내서 정답에 적재. 이후 대기큐에서 꺼내서 작업 재개
                if time == working[0][0] + working[0][-1]:
                    complete_job = working.popleft()
                    answer.append(time - complete_job[1])
                    job = heapq.heappop(queue)
                    working.append((time, job[1], job[0]))
                # 작업이 끝날 시점이 아니면 작업이 끝날 시점으로 이동(시간 아끼기)
                else:
                    time = working[0][0] + working[0][-1]

            # 디스크가 작업 중이 아니면
            else:
                job = heapq.heappop(queue)
                # 작업 시작 시간, 작업 요청 시간, 작업 소요 시간
                working.append((time, job[1], job[0]))
                time = working[0][0] + working[0][-1]
                
        else: # 대기 중인 작업이 없고
            # 작업 중이면
            if working:
                if time == working[0][0] + working[0][-1]:
                    complete_job = working.popleft()
                    answer.append(time - complete_job[1])
                else:
                    time = working[0][0] + working[0][-1]

            else:
                time = jobs[0][1]
                
    return math.floor(sum(answer)/len(answer))