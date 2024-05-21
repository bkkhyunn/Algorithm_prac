import heapq
from itertools import combinations, combinations_with_replacement

def solution(k, n, reqs):
    answer = 9999999999
    # 중복 조합을 통해서 상담사들을 각 상담 유형에 따라 분배
    for comb in combinations(range(1, n), k-1):
        
        # 맨 처음 0, 맨 마지막 n 을 두고 1 이상 n-1 이하 중 k-1 개의 수를 뽑는다.
        # 그렇게 되면 인접한 인덱스의 값끼리 차이를 구했을 때 k 개의 값이 나온다.
        # 이는 각 상담 유형별 몇 명의 상담사가 배치되었는지를 나타낸다.
        consultant = [0, *comb, n]
        #print(consultant)
        
        # 특정 상담사 분배의 총 대기 시간
        total_wait = 0
        
        # heapq 를 통해 상담 유형 별 상담 리스트를 만든다. 각 유형별 리스트에는 특정 상담이 끝나는 시간을 넣는다.
        consult_list = [[] for _ in range(k+1)]
        for start, duration, consult in reqs:
            
            # 진행 중인 상담이 있고, 현재 상담 시작 시간이 진행 중 상담이 끝날 시간보다 크거나 같을 때
            while consult_list[consult] and consult_list[consult][0] <= start:
                # min heap 특성에 따라 가장 빨리 끝나는 진행 중인 상담을 제거한다.
                heapq.heappop(consult_list[consult])
            
            # 특정 상담 유형에 배정된 상담사 수만큼 진행 중인 상담이 있다면
            # 진행 중인 상담이 끝나고 현재 상담을 리스트에 집어넣는다.
            if len(consult_list[consult]) == consultant[consult] - consultant[consult-1]:
                # 현재 상담이 시작될 때까지 기다려야 하는 시간
                wait = heapq.heappop(consult_list[consult]) - start
                total_wait += wait
                start += wait
            
            heapq.heappush(consult_list[consult], start + duration)
        
        answer = min(answer, total_wait)
            
    return answer