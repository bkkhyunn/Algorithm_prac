# dfs
def solution(numbers, target):
    answer = 0
    
    def calc_sum(idx, summation):
        nonlocal answer
        
        if idx == len(numbers):
            if summation == target:
                answer += 1
            return
        
        calc_sum(idx+1, summation + numbers[idx])
        calc_sum(idx+1, summation - numbers[idx])
    
    calc_sum(0, 0)
        
    return answer