import re
from itertools import product

# 첫번째 풀이 (구현)
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

# 두번째 풀이 (개선)
def solution(user_id, banned_id):
    answer = 0
    s_user_id = str(user_id)
    #print(f'user_id 문자열 전환 : {s_user_id}')
    
    possible_list = []
    for ban_id in banned_id:
        pattern = "'" + ban_id.replace('*', '[a-z0-9]') + "'"
        possible_list.append(re.findall(pattern, s_user_id))
    #print(f'banned_id 별 가능한 user_id : {possible_list}')
    
    candidate = []
    for possible in product(*possible_list):
        # 모든 조합 중 동일 아이디 제거
        if len(possible) == len(set(possible)):
            # 모든 조합 중 같은 조합 제거
            if set(possible) not in candidate:
                candidate.append(set(possible))
                answer += 1
    
    return answer