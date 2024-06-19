# input 의 값이 매우 크기 때문에 이진탐색으로 도전
# 이진탐색의 기준값은 바위 사이 거리의 최소값
# 바위 사이의 거리를 기준으로 점점 줄여가면서, 제거되는 바위의 개수가 n 개일 때 최소값들 중 최대값을 구한다.
# 제거되는 바위의 개수가 n 개일 때 최솟값들 중 최댓값을 찾는다. 이에 start 를 증가시켜 범위를 높혀
# 반대 방향으로 탐색하여 최솟값들 중 최댓값을 찾아준다.

def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks += [distance]
    
    start, end = 0, distance  
    
    while start <= end:
        
        # 이번 탐색에서 원하는 바위 사이 거리의 최소값
        mid = (start + end) // 2  
        min_distance = float('inf')  
        current, rm_cnt = 0, 0
        
        for rock in rocks:
            diff = rock - current
            
            # 바위 사이의 거리가 이번 탐색에서 설정한 바위 사이의 거리보다 작다면 삭제
            # 최소값들 중 최대값을 찾아야 하기 때문
            if diff < mid:  
                rm_cnt += 1
                # n 보다 많이 바위를 제거했다면 반복문을 빠져나온다.
                if rm_cnt > n:
                    break
            
            # 바위 사이의 거리가 이번 탐색에서 설정한 바위 사이의 거리보다 크거나 같다면 다음 거리를 구한다.
            # 그리고 최소 거리를 계산할 current 를 갱신한다.
            else:  
                current = rock
                # 이진탐색에서 설정한 최소거리가 나오지 않을 수 있기 때문에 실제 최소값을 저장한다.
                min_distance = min(min_distance, diff)  
        
        # n 보다 많이 제거했다면 설정한 최소 거리가 너무 크다면 줄여준다.
        if rm_cnt > n:
            end = mid - 1
        
        # n 보다 적게 혹은 같게 제거했다면 정답을 최소거리로 갱신하고 최소값들 중 더 큰 값을 찾는다.
        else:  
            answer = min_distance
            start = mid + 1

    return answer