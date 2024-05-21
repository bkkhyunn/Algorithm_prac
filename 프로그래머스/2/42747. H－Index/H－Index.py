# 완전 탐색
def solution(citations):
    answer = 0
    for i in range(len(citations)+1):
        h = i
        c_paper, n_paper = 0, 0
        for citation in citations:
            if citation >= h:
                c_paper += 1
            else:
                n_paper += 1
        
        if c_paper >= h and n_paper <= h:
            answer = max(answer, h)
            
    return answer

# # 정렬
# def solution(citations):
#     citations.sort(reverse=True)
#     for i in range(len(citations)):
#         if citations[i] <= i+1:
#             return max(citations[i], i)
#     else:
#         return len(citations) 