# 처음 위상정렬을 생각했지만, 모든 순위를 정확히 알 수 없어서 어렵다.
# 또한 모든 경기 결과는 모순이 없고, A 가 B 를 이기고, B 가 C 를 이긴다면 A 는 C 를 이긴다. 즉 간접적 승패관계를 알아야 한다.
# 플로이드 와샬 알고리즘을 이용해서 문제를 풀 수 있다.

def solution(n, results):
    # 2차원 리스트를 이용하여 그래프 초기화
    # wins[i][j]는 i 선수가 j 선수를 이겼다는 의미
    wins = [[False] * (n + 1) for _ in range(n + 1)]
    
    for winner, loser in results:
        wins[winner][loser] = True
    
    # 플로이드-와샬 알고리즘을 통해 모든 쌍의 승패 관계를 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True
    
    # 각 선수에 대해 모든 다른 선수와의 승패를 알고 있는지 확인
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if wins[i][j] or wins[j][i]:
                count += 1
        if count == n - 1:  # 다른 모든 선수와의 관계를 알고 있는 경우
            answer += 1
    
    return answer