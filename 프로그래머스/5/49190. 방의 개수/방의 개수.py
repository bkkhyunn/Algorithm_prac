# 오일러 지표 활용
# 평면그래프에서 점의 개수(v) - 선의 개수(e) + 면의 개수(f) = 1 이다.
# 여기서 면의 개수가 방의 개수가 된다.
# 중요한 것은 선이 교차하면, 교차점으로 점이 1개 생기고, 그 점으로부터 시작되는 선이 4개 생김에 유의해야 한다.

def solution(arrows):
    
    # 0 에서 7 까지 방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    # 노드, 간선
    v_set, e_set = set(), set()
    v, e = 0, 0
    
    # 시작점
    x, y = 0, 0
    v_set.add((x, y))
    
    for arrow in arrows:
        
        # 현재 노드(x,y) 에서 이동할 노드(nx, ny)
        nx = x + dx[arrow]
        ny = y + dy[arrow]
        opp = (arrow+4) % 8 # arrow 의 반대방향
        
        # 현재(x, y) 에서 다음(nx, ny)로 가는 간선(arrow), 다음에서 현재로 오는 간선(arrow 반대 opp)
        if ((x, y, arrow) not in e_set) and ((nx, ny, opp) not in e_set):
            
            if arrow % 2: # 대각선일 때 다른 대각선과 교차하는 지점이 있는지 확인

                # 1) 현재에서 (arrow-1) 방향으로 이동한 점에서 (arrow+2) 방향으로 이동하는 간선과 교차하는지
                case_1 = ((x + dx[arrow-1]), (y + dy[arrow-1]), (arrow+2)%8)
                # 2) 현재에서 (arrow+1) 방향으로 이동한 점에서 (arrow-2) 방향으로 이동하는 간선과 교차하는지
                case_2 = (x + dx[(arrow + 1)%8], y + dy[(arrow + 1)%8], (arrow-2)%8)
                
                # 교차되는 대각선이 지나간 간선에 있다면 
                if case_1 in e_set or case_2 in e_set:
                    e += 2 # 간선은 총 4개가 생긴다.(대각선 2개는 이미 e_set에 있기 때문에 2를 더한다.)
                    v += 1 # 점은 1개가 생긴다.
            
            v_set.add((nx, ny))
            e_set.add((x, y, arrow))
        
        # 좌표 갱신
        x = nx
        y = ny
    
    # 점과 선의 개수를 더한다.
    v += len(v_set)
    e += len(e_set)
    
    # 오일러 지표대로 리턴
    return 1 + e - v