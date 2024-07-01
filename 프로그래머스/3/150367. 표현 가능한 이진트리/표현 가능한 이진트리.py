def solution(numbers):
    answer = []
    
    def check(b):
        
        if root := (len(b) // 2):
        
            if b[root] == '0' and ('1' in b):
                return False
        
            else:
                return check(b[:root]) and check(b[root+1:])
        else:
            return True
    
    for num in numbers:
        b = bin(num)[2:]
        i = 0
        while len(b) > (2**i-1):
            i += 1
            
        b = b.rjust((2**i-1), '0')
        #print(b)
        
        answer.append(int(check(b)))
        
    return answer