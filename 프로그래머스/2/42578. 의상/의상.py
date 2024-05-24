from collections import Counter

def solution(clothes):
    answer = 1
    
    counter = Counter([cloth_type for _, cloth_type in clothes])
    
    for val in counter.values():
        answer *= (val+1)
        
    return answer - 1