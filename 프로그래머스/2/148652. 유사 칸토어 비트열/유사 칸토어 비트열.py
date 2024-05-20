# 11011 에서 0 은 항상 5로 나눴을 때 나머지 2 인 자리에 있다.
# 예를 들어 1101111011 에서 0 은 2, 7 에 위치한다.
# 00000 은 그 인덱스를 5로 계속 나눠줬을 떄 나머지가 2에 도달한다.
# 결국 무수히 많은 칸토어 비트열이 있더라도, 이는 항상 5묶음으로 생각할 수 있기 때문에, 5로 계속 나눠주면서
# 나머지가 2이면 0, 아니면 1이라 생각할 수 있다.

def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        while i > 0:
            i, mod = divmod(i, 5)
            if mod == 2:
                break
        else:
            answer += 1
            
    return answer