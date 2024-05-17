from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    answer = []
    
    # a, b 주사위 선택
    n = len(dice)
    a_dice = list(combinations(range(n), n // 2))
    b_dice = list(combinations(range(n), n // 2))[::-1]
    
    # 승 수 구하기. bisect 를 통해 시간 감소시키기
    max_win, a_win = 0, 0
    for a, b in zip(a_dice, b_dice):
        a_dices = list(map(lambda x: dice[x], a))
        b_dices = list(map(lambda x: dice[x], b))
        a_res, b_res = [], []
        
        for i in product(*a_dices):
            a_res.append(sum(i))
        for i in product(*b_dices):
            b_res.append(sum(i))
            
        b_res.sort()
        l = len(b_res)
        
        for i in a_res:
            r = bisect_left(b_res, i)
            #print(r)
            a_win += r
            
        if max_win < a_win:
            max_win = a_win
            answer = sorted(map(lambda x: x+1, [*a]))
            a_win = 0
            
        a_win = 0
        
    return answer