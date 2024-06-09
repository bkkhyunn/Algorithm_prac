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

    banned_id = ["'" + _.replace('*', '[a-z0-9]') + "'"  for _ in banned_id]
    #print(f'banned_id 정규식 전환 : {banned_id}')
    
    s_user_id = str(user_id)
    #print(f'user_id 문자열 전환 : {s_user_id}')
    
    possible_list = [re.findall(_, s_user_id) for _ in banned_id]   
    #print(f'banned_id 별 가능한 user_id : {possible_list}')
    
    possible_list = list(product(*possible_list))
    #print(f'banned_id 별 가능한 user_id 의 모든 조합 : {possible_list}')
    
    possible_list = [frozenset(p) for p in possible_list if len(set(p)) == len(p)]
    #print(f'banned_id 별 가능한 user_id 의 모든 조합 중 동일 아이디 제거 : {possible_list}')
    
    possible_list = set(possible_list)
    #print(f'banned_id 별 가능한 user_id 의 모든 조합 중 중복 제거 : {possible_list}')
    
    return len(possible_list)