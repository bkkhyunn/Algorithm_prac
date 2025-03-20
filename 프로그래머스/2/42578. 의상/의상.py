from collections import Counter
import math

def solution(clothes):
    
    temp = [cloth_type for cloth, cloth_type in clothes]
    counter_dict = Counter(temp)
    
    answer = math.prod([value + 1 for value in counter_dict.values()]) - 1
    
    return answer