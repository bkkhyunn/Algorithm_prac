import heapq

def solution(operations):
    
    heap = []
    for operation in operations:
        
        command, data = operation.split()
        #print(heap)
        if command == 'I':
            heapq.heappush(heap, int(data))
        else:
            if heap:
                if int(data) == 1:
                    #heap = sorted(heap)[:-1]
                    val = heapq.nlargest(1, heap)[0]
                    heap.remove(val)
                elif int(data) == -1:
                    heapq.heappop(heap)
            else:
                continue
    
    return [max(heap),min(heap)] if heap else [0,0]