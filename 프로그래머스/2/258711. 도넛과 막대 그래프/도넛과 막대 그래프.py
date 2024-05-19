from collections import defaultdict

def solution(edges):
    new, donut, stick, eight = 0,0,0,0
    # 각 노드별로 나가는 간선(start), 들어오는 간선(end)
    graph = defaultdict(lambda: [0,0])
    for start, end in edges:
        graph[start][0] += 1
        graph[end][1] += 1
        
    #print(graph)
    
    for node, info in graph.items():
        start, end = info
        
        # 새로운 정점: start 가 2(도형의 개수) 이상, end 가 0
        if start >= 2 and end == 0:
            new = node
        
        # stick: start 0, end 1
        elif start == 0 and end >= 1:
            stick += 1
            
        # eight
        elif start >= 2 and end >= 2:
            eight += 1
    
    # donut
    donut = graph[new][0] - (stick + eight)
        
    return [new, donut, stick, eight]