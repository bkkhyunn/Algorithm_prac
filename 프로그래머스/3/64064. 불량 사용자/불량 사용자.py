import re
from itertools import product

def solution(user_id, banned_id):
    answer = 0
    possibles = []
    
    for ban in banned_id:
        cnt = 0
        pattern = ban.replace('*', '[a-z0-9]')
        possible = []
        for user in user_id:
            if [user] == re.findall(pattern, user):
                possible.append(user)
        
        if possible:
            possibles.append(possible)
    
    candidate = []
    for cand in product(*possibles):
        if len(cand) == len(set(cand)):
            if set(cand) not in candidate:
                candidate.append(set(cand))
                answer += 1
    
    return answer