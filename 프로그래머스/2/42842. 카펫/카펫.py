def solution(brown, yellow):
    answer = []
    total_grid = brown + yellow
    cand = []
    
    for i in range(1, (int(yellow**(1/2)) + 1)):
        if yellow % i == 0:
            cand.append((yellow // i, i))
    #print(cand)
    for w, h in cand:
        if (w+2) * (h+2) == total_grid:
            answer = [w+2, h+2]
        
    return answer