import re
from itertools import product

# 구현 문제인 것 같다.
def solution(user_id, banned_id):
    answer = 0
    possibles = []
    
    for ban in banned_id:
        # 불량 사용자 아이디 목록을 정규식을 사용할 수 있게 패턴화 한다.
        pattern = ban.replace('*', '[a-z0-9]')
        
        # 불량 사용자 아이디 한 개에 해당할 수 있는 유저 아이디를 담는다.
        possible = []
        for user in user_id:
            if [user] == re.findall(pattern, user):
                possible.append(user)
        
        if possible:
            possibles.append(possible)
    
    #print(possibles)
    # 순서에 따라 중복을 제거해주기 위해서 아래 과정을 거친다.
    candidate = []
    for cand in product(*possibles):
        if len(cand) == len(set(cand)):
            if set(cand) not in candidate:
                candidate.append(set(cand))
                answer += 1
    
    return answer