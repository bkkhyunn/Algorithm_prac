# 아이디어
# times 중 가장 오래 걸리는 시간 * 입국 인원 을 하면 가능한 가장 큰 시간이 나온다.
# 이를 기준으로 이진 탐색을 실시.
# 즉 시간을 배열로 보고, 계속해서 중간 시간에 최대 몇 명을 처리할 수 있는지 계산한다.

def solution(n, times):
    times.sort()
    # 시작점, 끝점
    start = 0
    end = times[-1] * n
    
    def binary_search(start, end):
        nonlocal times, n
        
        cnt = 0
        answer = -1

        while start <= end:
            mid = (start + end) // 2
            cnt = 0

            # mid 시간 안에 각 심사관 별로 해당 시간에 몇 명을 처리할 수 있는지
            for time in times:
                cnt += mid // time
            
            # 입국 심사 인원보다 더 많이 처리할 때
            if cnt >= n:
                
                # 정답 최신화
                if answer == -1:
                    answer = mid
                else:
                    answer = min(answer,mid)
                
                # 끝 시간을 중간 시간보다 1 작게 최신화
                end = mid - 1
            
            # 입국 심사 인원보다 더 적게 처리할 때
            else:
                # 시작 시간을 중간 시간보다 1 크게 최신화
                start = mid + 1

        return answer
    
    answer = binary_search(start, end)
    return answer