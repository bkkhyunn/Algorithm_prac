# # from collections import defaultdict

# # MAX = 100001
# # MIN = -1
# # TREE_DEPTH = 0

# # def solution(nodeinfo):
# #     global TREE_DEPTH

# #     pre_tree = defaultdict(list)
# #     post_tree = defaultdict(list)
# #     level = set()

# #     for i in range(len(nodeinfo)):
# #         x, y = nodeinfo[i]
# #         pre_tree[y].append((x, i+1))
# #         post_tree[y].append((x, i+1))
# #         level.add(y)

# #     for i in level:
# #         pre_tree[i].sort(reverse=True)
# #         post_tree[i].sort(reverse=True)

# #     level = sorted(list(level), reverse=True)
# #     TREE_DEPTH = len(level)
    
# #     preorder = []
# #     pre_order(MIN, MAX, 0, preorder, pre_tree, level)
# #     postorder = []
# #     post_order(MIN, MAX, 0, postorder, post_tree, level)

# #     return [preorder, postorder]


# # def pre_order(left, right, depth, result, tree, level):
# #     if depth == TREE_DEPTH:
# #         return
# #     if len(tree[level[depth]]) <= 0:
# #         return
# #     if not (left < tree[level[depth]][-1][0] < right):
# #         return
    
# #     x, index = tree[level[depth]].pop()
# #     result.append(index)
# #     pre_order(left, x, depth+1, result, tree, level)
# #     pre_order(x, right, depth+1, result, tree, level)


# # def post_order(left, right, depth, result, tree, level):
# #     if depth == TREE_DEPTH:
# #         return
# #     if len(tree[level[depth]]) <= 0:
# #         return
# #     if not (left < tree[level[depth]][-1][0] < right):
# #         return
    
# #     x, index = tree[level[depth]].pop()
# #     post_order(left, x, depth+1, result, tree, level)
# #     post_order(x, right, depth+1, result, tree, level)
# #     result.append(index)

# from sys import setrecursionlimit
# setrecursionlimit(10000)

# def solution(nodeinfo): ### ↓ n:노드번호 추가하여 (x,y,n) 형태로 x좌표 기준 정렬
#     nodeinfo = sorted([(x,y,i+1) for i,(x,y) in enumerate(nodeinfo)], key=lambda x:x[0])
#     result = [[], []]

#     def REC(nodeinfo):
#         if nodeinfo:
#             highest = (0,-1,0) ### 루트 노드 정보: (nodeinfo 에서 index, y, 노드번호)
#             for idx, (x,y,n) in enumerate(nodeinfo): ### 루트 노드 idx 찾기 (3분할 과정)
#                 if y > highest[1]:
#                     highest = (idx, y, n)

#             result[0].append(highest[-1]) ### 좌,우 재귀함수 실행전 루트노드 탐색 --> 전위 순회
#             left, right = nodeinfo[:highest[0]], nodeinfo[highest[0]+1:]
#             REC(left), REC(right)
#             result[1].append(highest[-1]) ### 좌,우 재귀함수 실행후 루트노드 탐색 --> 후위 순회
#     REC(nodeinfo)
#     return result
#10:57
import sys
sys.setrecursionlimit(10**6)
class BTREE:
    '''
    1. 2진 트리 class 를 만든다
        1. Node 에는 (left, right) 연결구조
        2. Node 에는 value와 인덱스
        3. left 혹은 right 가 비어있으면 해당 자리에 None, default는 None
        4. 신규 삽입시 left 혹은 right 에 Node 할당
        5. 할당 된 Node에 value, 인덱스 값 지정
    2. 2진 트리에 nodeinfo에 있는 node정보에 따라 할당
        1, x[1] 을 기준으로 일단 정렬, reverse
        2. 첫번째 노드는 루트로 리스트 btree 에 원소의 인덱스와 같이 [idx, x좌표, y좌표] 삽입
        3. 두번째 노드부터는 btree의 node들과 비교 x좌표가 작으면 left에 할당, 아니면 right에 할당
    '''
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
    def insert(self, val):
        if self.root is None:
            self.root = val
        else:
            if self.root[1] > val[1]:
                if self.left is None:
                    self.left = BTREE()
                    self.left.insert(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = BTREE()
                    self.right.insert(val)
                else:
                    self.right.insert(val)

def preorder(data):
    '''
    1. 비어 있을 경우 [] return
    2. 자기자신을 먼저 방문후 left, right 순으로 방문 [root[0]] + preorder(left) + preorder(right)
    '''
    if data is None:
        return []
    return [data.root[0]] + preorder(data.left) + preorder(data.right)

def postorder(data):
    '''
    1. 비어 있을 경우 [] return
    2. left를 먼저 방문, right 방문 그 후 자기자신 방문 순으로 반환 postorder(left) + postorder(right) + [root[0]]
    '''
    if data is None:
        return []
    return postorder(data.left) + postorder(data.right) + [data.root[0]]


def solution(nodeinfo):
    '''
    3. 중위순회, 전위순회 반환
    '''
    btree = BTREE()
    nodes = [[i+1,v[0], v[1]] for i,v in enumerate(nodeinfo) ]
    nodes = sorted(nodes, key = lambda x: x[2], reverse = True)
    for node in nodes:
        btree.insert(node)
    pre = preorder(btree)
    post = postorder(btree)
    answer = []
    answer.append(pre)
    answer.append(post)
    return answer