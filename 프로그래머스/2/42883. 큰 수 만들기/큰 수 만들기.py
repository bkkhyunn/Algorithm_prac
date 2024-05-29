# 그리디 사용하는 정당성은, 수를 하나씩 제거할 때마다 자리수는 동일하고, 수는 앞자리에 큰 수가 올수록 크기 때문에
# 앞에서부터 하나씩 확인하면서 다음 자리 수가 더 크면 그 수를 삭제하면 된다.
# 주어진 수가 계속해서 앞의 수가 뒤의 수보다 크게 넘어가서 k 가 남는 경우, 뒤에서 k 개 만큼 자르면 된다.

def solution(number, k):
    
    idx = 0
    
    while k > 0 and idx < len(number)-1:
        if number[idx] < number[idx+1]:
            number = number[:idx] + number[idx+1:]
            k -= 1
            # idx 를 바로 0으로 초기화하기 보다 앞의 수는 이미 확인 했으니 1개 없앤 것을 반영
            if idx != 0:
                idx -= 1
        else:
            idx += 1
    
    if k > 0:
        number = number[:-k]
            
    return number