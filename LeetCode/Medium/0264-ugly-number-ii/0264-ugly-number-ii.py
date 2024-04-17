import heapq

class Solution:    
    def nthUglyNumber(self, n: int) -> int:
        h = []
        answer = []
        heapq.heappush(h, 1)
        while len(answer) < n:
            cur = heapq.heappop(h)
            if len(answer) > 0 and answer[-1] == cur:
                continue
            heapq.heappush(h, cur*2)
            heapq.heappush(h, cur*3)
            heapq.heappush(h, cur*5)
            answer.append(cur)

        return answer[n-1]