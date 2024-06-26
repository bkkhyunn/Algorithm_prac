# 모든 간선 비용이 1 일 때 다익스트라. 시작 노드는 1번 노드
import heapq

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
    
    for v in edge:
        start, end = v
        # start 노드에서 end 노드까지 비용은 1. 양방향 고려
        graph[start].append((end, 1))
        graph[end].append((start, 1))
        
    def dijkstra(start):
        queue = []
        
        # 시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
        heapq.heappush(queue, (0, start))
        distance[start] = 0

        # queue 가 비어있지 않다면
        while queue:
            
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(queue)

            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]

                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost

                    # 값이 갱신되면 우선순위 큐에 해당 정보 기록
                    heapq.heappush(queue, (cost, i[0]))
        
    dijkstra(1)
    #print(distance)
        
    return distance.count(max(distance[1:]))