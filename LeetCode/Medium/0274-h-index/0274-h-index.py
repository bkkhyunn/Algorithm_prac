import bisect

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        answer = 0
        
        
        while h < max(citations):
            
            idx = bisect.bisect_left(citations, h)
            if n - idx >= h:
                answer = max(answer, h)
            #print(h, answer)
            h += 1
            
        return answer
    

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0