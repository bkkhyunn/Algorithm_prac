# 자식은 1인데 부모(루트)가 0 이면 불가능한 경우.

def solution(numbers):
    answer = []
    
    # 만들 수 있는지 없는지 판단하는 함수
    def check(b):
        
        if len(b) >= 3:
            root = (len(b) // 2)
             # 부모(루트)는 0인데 자식이 1이 하나라도 있는 경우 만들 수 없다.
            if b[root] == '0' and ('1' in b):
                return False
            # 부모(루트)가 1인 경우 더 작은 서브트리로 넘어간다.
            else:
                return check(b[:root]) and check(b[root+1:])
        # 트리의 길이가 3보다 적으면 확인할 필요 없다.
        else:
            return True
    
    for num in numbers:
        b = bin(num)[2:]
        
        # 포화 이진 트리 만들기
        i = 0
        while len(b) > (2**i-1):
            i += 1
        
        b = b.rjust((2**i-1), '0') # 오른쪽부터 첫번째 인자의 길이만큼 두번째 인자를 채운다.
        #print(b)
        
        answer.append(int(check(b)))
        
    return answer