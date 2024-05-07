from collections import Counter

# def solution(topping):
#     answer = 0
#     for i in range(1, len(topping)-1):
#         chul = topping[:i]
#         bro = topping[i:]
#         if len(set(chul)) == len(set(bro)):
#             answer += 1
#
#     return answer

def solution(topping):
    answer = 0
    chul = Counter(topping)
    bro = set()
    for i in topping:
        chul[i] -= 1
        bro.add(i)
        if chul[i] == 0:
            chul.pop(i)
        if len(chul) == len(bro):
            #print(chul)
            answer += 1
    
    return answer