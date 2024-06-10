# 알파벳 이동은 정해져있다. 커서 좌우 이동을 최적화 하는 문제.

def solution(name):
    answer = 0

    length = len(name)
    # 현재 위치 전에 가장 마지막 'A' 가 아닌 글자 위치, 이동 횟수
    save, move = 0, float('inf')
    
    # 알파벳 이동 횟수를 구하는 함수
    def top_down_curser(c):
        return min(ord('Z') - ord(c) + 1, ord(c) - ord('A'))
    
    for i in range(length):
        # 'A' 가 아닐 때만 
        if name[i] != 'A':
            answer += top_down_curser(name[i])
            
            if i == 0:
                continue
            
            # 전 저장 위치에서 거꾸로 진행했을 때 현재 위치까지 도달하는데 이동 횟수
            # 즉 전 저장 위치에서 반대 방향으로 갔을 때 현재 위치까지 이동 횟수이다.
            reverse = save + length - i
            # save + reverse : 정방향으로 가다가 거꾸로 진행했을 때 현재 위치까지 이동횟수
            # length - i + reverse : 거꾸로 가다가 정방향으로 진행했을 때 현재 위치까지 이동횟수
            move = min(move, min(save + reverse, length - i + reverse))
            #print(i, save, reverse, move)
            # save : 정방향으로 갔을 때의 이동횟수(다음 반복문에서 전 저장위치가 된다.)
            save = i
    
    # 정방향으로 그냥 갔을 때와 정방향 + 역방향 조합 비교
    move = min(save, move)
    return answer + move