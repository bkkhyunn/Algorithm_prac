from collections import Counter

def solution(nums):
    answer = len(nums)//2 if len(nums)//2 < len(set(nums)) else len(set(nums))
    
    return answer