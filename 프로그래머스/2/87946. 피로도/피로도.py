from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for possible in permutations(dungeons, len(dungeons)):
        tired = k
        clear = 0
        
        for dungeon in possible:
            required, consumption = dungeon
            
            if required <= tired and tired >= consumption:
                tired -= consumption
                clear += 1
                
        answer = max(answer, clear)
        
    return answer