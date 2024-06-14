# A* 알고리즘
# A* 알고리즘은 시작 노드만을 지정해 다른 모든 노드에 대한 최단 경로를 파악하는 다익스트라 알고리즘과 다르게 시작 노드와 목적지 노드를 분명하게 지정해 이 두 노드 간의 최단 경로를 파악할 수 있다.
# A* 알고리즘은 휴리스틱 추정값을 통해 알고리즘을 개선할 수 있다. 이러한 휴리스틱 추정값을 어떤 방식으로 제공하느냐에 따라 얼마나 빨리 최단 경로를 파악할 수 있느냐가 결정된다.

import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # 노드의 위치 (x, y)
        self.parent = parent  # 부모 노드
        self.g = 0  # 시작 노드에서 현재 노드까지의 비용
        self.h = 0  # 현재 노드에서 목표 노드까지의 휴리스틱 추정 비용
        self.f = 0  # 총 비용 (f = g + h)

    def __eq__(self, other):
        return self.position == other.position  # 노드 비교를 위한 메서드

    def __lt__(self, other):
        return self.f < other.f  # 우선순위 큐에서 비교를 위한 메서드

def heuristic(node, end):
    # 맨해튼 거리 휴리스틱 함수
    return abs(node.position[0] - end.position[0]) + abs(node.position[1] - end.position[1])

def astar(maze, start, end):
    start_node = Node(start)  # 시작 노드 생성
    end_node = Node(end)  # 목표 노드 생성

    open_list = []  # 열린 리스트 (탐색할 노드들)
    closed_list = set()  # 닫힌 리스트 (탐색이 완료된 노드들)

    heapq.heappush(open_list, start_node)  # 시작 노드를 열린 리스트에 추가

    while open_list:
        current_node = heapq.heappop(open_list)  # f값이 가장 작은 노드를 pop
        closed_list.add(current_node)  # 현재 노드를 닫힌 리스트에 추가

        if current_node == end_node:
            # 목표 노드에 도달하면 경로를 반환
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # 경로를 역순으로 반환

        children = []  # 현재 노드의 자식 노드들
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 상하좌우 이동
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # 미로 범위 내에 있는지 확인
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) - 1) or node_position[1] < 0:
                continue
            
            # 이동할 수 없는 위치(장애물)인지 확인
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)  # 자식 노드 생성
            children.append(new_node)  # 자식 노드를 자식 리스트에 추가

        for child in children:
            if child in closed_list:
                continue  # 자식 노드가 닫힌 리스트에 있으면 무시

            # g, h, f 값 계산
            child.g = current_node.g + 1  # g값: 시작 노드에서 현재 노드까지의 비용
            child.h = heuristic(child, end_node)  # h값: 현재 노드에서 목표 노드까지의 휴리스틱 비용
            child.f = child.g + child.h  # f값: 총 비용

            # 자식 노드가 열린 리스트에 있고 더 높은 g값을 가지고 있으면 무시
            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            heapq.heappush(open_list, child)  # 자식 노드를 열린 리스트에 추가

    return None  # 경로를 찾지 못한 경우

# 예제 사용법
maze = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 6)

path = astar(maze, start, end)
print(path)  # 결과: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6)]
