import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        if op.startswith('I'):
            num = int(op.split()[-1])
            heapq.heappush(heap, num)
        
        elif heap and (op == 'D -1'):
            heapq.heappop(heap)
        
        elif heap and (op == "D 1"):
            val = heapq.nlargest(1, heap)[0]
            heap.remove(val)

    return [max(heap), min(heap)] if heap else [0,0]