import heapq

def solution(operations):
    
    heap = []
    for operation in operations:
        
        command, data = operation.split()
        
        if command == 'I':
            heapq.heappush(heap, int(data))
        else:
            if heap:
                if int(data) == 1:
                    heap = heap[:-1]
                elif int(data) == -1:
                    heapq.heappop(heap)
            else:
                continue
    
    return [max(heap),min(heap)] if heap else [0,0]