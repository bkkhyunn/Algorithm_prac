class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        정렬 후 선형 탐색
        '''
        citations.sort(reverse=True) # 6, 5, 3, 1, 0
        n = len(citations) # h 의 최대값
        i, answer = 0, 0
        
        # i+1 은 h 이상 인용된 논문의 개수, citations[i] 는 인용된 횟수 h
        while i+1 <= n and i+1 <= citations[i]:
            answer = i+1
            i+=1
            
        return answer 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        Binary Search
        '''
        citations.sort(reverse=True)

        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (right + left) // 2
            if citations[mid] == mid:
                return mid
            elif citations[mid] > mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        Counting Sort
        '''
        n = len(citations)
        count = [0] * (n+1)

        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1
        
        total  = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i