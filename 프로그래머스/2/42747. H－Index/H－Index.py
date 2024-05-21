# def solution(citations):
#     answer = 0
#     for i in range(len(citations)+1):
#         h = i
#         c_paper, n_paper = 0, 0
#         for citation in citations:
#             if citation >= h:
#                 c_paper += 1
#             else:
#                 n_paper += 1
        
#         if c_paper >= h and n_paper <= h:
#             answer = max(answer, h)
            
#     return answer


# 다른 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0