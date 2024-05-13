# 어피치보다 라이언이 1발 더 많이 맞추거나 아예 안 맞추거나

def solution(n, info):
    answer = [-1]
    a_info = info
    l_info = [0] * len(info)
    gap = 0
    
    def calc_score(a_info, l_info):
        # 어피치, 라이언 총 점수
        a_score = 0
        l_score = 0
        
        for i in range(len(a_info)):
            if a_info[i] > 0 or l_info[i] > 0:
                if a_info[i] >= l_info[i]:
                    a_score += (10-i)
                else:
                    l_score += (10-i)
        return (l_score > a_score, l_score - a_score)
    
    def dfs(idx, cnt):
        nonlocal answer, a_info, l_info, gap
        
        if cnt == 0 or idx == 11:
            result = calc_score(a_info, l_info)
            # 라이언이 어피치보다 점수가 높을 때
            if result[0]:
                
                # 화살이 남은 경우, 0점에 다 쏴도 이긴다.
                if cnt >= 0:
                    l_info[10] = cnt
                    
                if result[1] > gap:
                    gap = result[1]
                    answer = l_info.copy()
                
                elif result[1] == gap:
                    for i in range(len(l_info)):
                        if l_info[10-i] > answer[10-i]:
                            answer = l_info.copy()
                            break
                        elif l_info[10-i] < answer[10-i]:
                            answer = answer
                            break
            return
        
        # 어피치보다 1개 더 많이 맞추거나, 아예 안 맞추거나
        if cnt > a_info[idx]:
            # 1개 더 많이 맞춘 걸로 진행
            l_info[idx] = a_info[idx]+1
            dfs(idx+1, cnt-(a_info[idx]+1))
            
        # 아예 안 맞추는 걸로 진행
        l_info[idx] = 0
        dfs(idx+1, cnt)
        
    dfs(0, n)
    
    return answer