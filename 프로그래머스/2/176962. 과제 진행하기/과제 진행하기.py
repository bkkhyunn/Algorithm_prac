def solution(plans):
    
    # 계산 편의성을 위해 분으로 맞추기
    for p in plans:
        p[1] = (int(p[1].split(':')[0]) * 60) + int(p[1].split(':')[1])
        p[2] = int(p[2])
    
    # 제일 먼저 해야 하는 과제 순으로 정렬
    plans.sort(key=lambda x: x[1])
    
    # 완료한 과제, 멈춰둔 과제
    complete, stop = [], []
    plans_count = len(plans)
    idx = 0
    time = plans[idx][1]
    
    while len(complete) != plans_count:
        
        # 모든 plans 를 다 돌았는데 아직 남은 과제가 있는 경우, 가장 최근의 멈춘 과제부터 완료
        if idx == plans_count - 1:
            complete.append(plans[idx][0])
            for assignment, _ in stop[::-1]:
                complete.append(assignment)
        
        # plans 돌면서 조건에 맞게 진행
        else:
            # 과제, 걸리는 시간
            assignment, duration = plans[idx][0], plans[idx][2]
            
            # 현재 시각에서 해당 과제가 걸리는 시간을 더한 것이 다음 과제 시작 시간보다 클 때
            if time + duration > plans[idx+1][1]:
                # 현재 과제와 해당 과제의 남은 시간을 멈춘 목록에 삽입
                stop.append([assignment, duration-(plans[idx+1][1]-time)])
                # 다음 과제 시작 시간으로 업데이트
                time = plans[idx+1][1]
                
            # 현재 시각에서 해당 과제가 걸리는 시간을 더한 것이 다음 과제 시작 시간과 같을 때
            elif time + duration == plans[idx+1][1]:
                complete.append(assignment)
                time = plans[idx+1][1]
                
            # 현재 시각에서 해당 과제가 걸리는 시간을 더한 것이 다음 과제 시작 시간보다 작을 때(시간 남을 때)
            elif time + duration < plans[idx+1][1]:
                complete.append(assignment)
                time += duration
                # 다음 과제 시작 전까지 남은 시간
                extra = plans[idx+1][1] - time
                
                while stop and extra != 0:
                    # 가장 최근 멈춘 과제의 남은 시간이 다음 과제 시작 전까지 남은 시간보다 작을 경우
                    if stop[-1][1] <= extra:
                        extra -= stop[-1][1]
                        complete.append(stop.pop()[0])
                    # 가장 최근 멈춘 과제의 남은 시간이 다음 과제 시작 전까지 남은 시간보다 많을 경우
                    else:
                        stop[-1][1] -= extra
                        extra = 0
                
                time = plans[idx+1][1]
        idx += 1
            
    return complete