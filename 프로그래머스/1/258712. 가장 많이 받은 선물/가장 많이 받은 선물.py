from collections import deque

def solution(friends, gifts):
    answer = 0
    # (나에게 받은 사람: 선물 개수), (나에게 준 사람: 선물 개수)
    log = {friend : [{friend : 0 for friend in friends}, {friend : 0 for friend in friends}] for friend in friends}
    gift_num = {friend : 0 for friend in friends}
    
    for gift in gifts:
        give, take = gift.split()
        log[give][0][take] += 1
        log[take][1][give] += 1
    
    queue = deque(friends)
    while len(queue) > 1:
        friend = queue.popleft()
        
        for other in queue:
            
            if friend == other:
                continue
            
            if log[friend][0][other] > log[other][0][friend]:
                gift_num[friend] += 1
            
            elif log[friend][0][other] == log[other][0][friend]:
                f_n = sum(log[friend][0].values()) - sum(log[friend][1].values())
                o_n = sum(log[other][0].values()) - sum(log[other][1].values())
                
                if f_n > o_n:
                    gift_num[friend] += 1
                elif f_n == o_n:
                    continue
                else:
                    gift_num[other] += 1
            else:
                gift_num[other] += 1
    
    return max(gift_num.values())