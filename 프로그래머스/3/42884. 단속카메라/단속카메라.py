# 하나의 카메라가 최대한 많은 차량을 만나야 한다. 
def solution(routes):
    answer = 1
    routes.sort()
    
    # 하나의 카메라 설치 범위
    # 반복문에서 left 가 right 보다 크면 다른 카메라가 필요하다고 볼 수 있다.
    left, right = -30000, 30000
    
    for route in routes:
        start, end = route
        
        # left 는 계속해서 갱신된다. routes 를 정렬했기 때문.
        left = start
        
        # 차량 진출 지점이 카메라 오른쪽 끝 범위보다 작거나 같으면 카메라 범위를 갱신한다.
        if end <= right:
            right = end
        
        # left 가 right 보다 크면 카메라가 하나 더 필요하고, 해당 카메라의 범위를 갱신시킨다.
        if right - left < 0:
            answer += 1
            right = end
    
    return answer