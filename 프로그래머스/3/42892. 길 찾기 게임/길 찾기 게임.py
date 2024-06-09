# from collections import defaultdict

# MAX = 100001
# MIN = -1
# TREE_DEPTH = 0

# def solution(nodeinfo):
#     global TREE_DEPTH

#     pre_tree = defaultdict(list)
#     post_tree = defaultdict(list)
#     level = set()

#     for i in range(len(nodeinfo)):
#         x, y = nodeinfo[i]
#         pre_tree[y].append((x, i+1))
#         post_tree[y].append((x, i+1))
#         level.add(y)

#     for i in level:
#         pre_tree[i].sort(reverse=True)
#         post_tree[i].sort(reverse=True)

#     level = sorted(list(level), reverse=True)
#     TREE_DEPTH = len(level)
    
#     preorder = []
#     pre_order(MIN, MAX, 0, preorder, pre_tree, level)
#     postorder = []
#     post_order(MIN, MAX, 0, postorder, post_tree, level)

#     return [preorder, postorder]


# def pre_order(left, right, depth, result, tree, level):
#     if depth == TREE_DEPTH:
#         return
#     if len(tree[level[depth]]) <= 0:
#         return
#     if not (left < tree[level[depth]][-1][0] < right):
#         return
    
#     x, index = tree[level[depth]].pop()
#     result.append(index)
#     pre_order(left, x, depth+1, result, tree, level)
#     pre_order(x, right, depth+1, result, tree, level)


# def post_order(left, right, depth, result, tree, level):
#     if depth == TREE_DEPTH:
#         return
#     if len(tree[level[depth]]) <= 0:
#         return
#     if not (left < tree[level[depth]][-1][0] < right):
#         return
    
#     x, index = tree[level[depth]].pop()
#     post_order(left, x, depth+1, result, tree, level)
#     post_order(x, right, depth+1, result, tree, level)
#     result.append(index)

from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(nodeinfo): ### ↓ n:노드번호 추가하여 (x,y,n) 형태로 x좌표 기준 정렬
    nodeinfo = sorted([(x,y,i+1) for i,(x,y) in enumerate(nodeinfo)], key=lambda x:x[0])
    result = [[], []]

    def REC(nodeinfo):
        if nodeinfo:
            highest = (0,-1,0) ### 루트 노드 정보: (nodeinfo 에서 index, y, 노드번호)
            for idx, (x,y,n) in enumerate(nodeinfo): ### 루트 노드 idx 찾기 (3분할 과정)
                if y > highest[1]:
                    highest = (idx, y, n)

            result[0].append(highest[-1]) ### 좌,우 재귀함수 실행전 루트노드 탐색 --> 전위 순회
            left, right = nodeinfo[:highest[0]], nodeinfo[highest[0]+1:]
            REC(left), REC(right)
            result[1].append(highest[-1]) ### 좌,우 재귀함수 실행후 루트노드 탐색 --> 후위 순회
    REC(nodeinfo)
    return result