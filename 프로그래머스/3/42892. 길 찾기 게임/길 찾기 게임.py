## 1
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10000)

# 전체 트리의 x 값 범위
MIN, MAX = -1, 100001
# 전체 트리 깊이
TREE_DEPTH = 0

def solution(nodeinfo):
    global TREE_DEPTH

    # 전위, 중위, 후위 순위를 위한 트리를 각각 생성
    pre_tree = defaultdict(list)
    mid_tree = defaultdict(list)
    post_tree = defaultdict(list)
    # y값 level
    level = set()

    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        # 각 트리는 {y값 : [(해당 y값을 가진 노드의 x 좌표와 노드번호),...]}
        pre_tree[y].append((x, i+1))
        mid_tree[y].append((x, i+1))
        post_tree[y].append((x, i+1))
        level.add(y)

    for i in level:
        # x 값이 작은 것(왼쪽에 위치한 노드) 부터 판단하기 위하여 역순 정렬
        pre_tree[i].sort(reverse=True)
        mid_tree[i].sort(reverse=True)
        post_tree[i].sort(reverse=True)

    level = sorted(list(level), reverse=True)
    TREE_DEPTH = len(level)
    
    # 각 순회의 인자는 특정 순회 시 가능한 x 값의 최소, 최대, depth, 결과를 담을 리스트, 각 순회용 트리, level
    preorder = []
    pre_order(MIN, MAX, 0, preorder, pre_tree, level)
    midorder = []
    mid_order(MIN, MAX, 0, midorder, mid_tree, level)
    postorder = []
    post_order(MIN, MAX, 0, postorder, post_tree, level)

    return [preorder, postorder]


def pre_order(left, right, depth, result, tree, level):
    '''
    전위 순회
    Root -> L -> R
    '''
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return
    
    x, index = tree[level[depth]].pop()
    result.append(index)
    pre_order(left, x, depth+1, result, tree, level)
    pre_order(x, right, depth+1, result, tree, level)

def mid_order(left, right, depth, result, tree, level):
    '''
    중위 순회
    L -> Root -> R
    '''
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return
    
    x, index = tree[level[depth]].pop()
    mid_order(left, x, depth+1, result, tree, level)
    result.append(index)
    mid_order(x, right, depth+1, result, tree, level)

def post_order(left, right, depth, result, tree, level):
    '''
    후위 순회
    L -> R -> Root
    '''
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return
    
    x, index = tree[level[depth]].pop()
    post_order(left, x, depth+1, result, tree, level)
    post_order(x, right, depth+1, result, tree, level)
    result.append(index)

## 2

from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(nodeinfo):
    # 노드번호 추가하여 (x,y,n) 형태 만들고 x좌표 기준 정렬
    nodeinfo = sorted([(x,y,i+1) for i,(x,y) in enumerate(nodeinfo)], key=lambda x:x[0])
    result = [[], []]
    #print(nodeinfo)

    # 트리를 순회 하는 함수
    def make_order(nodeinfo):
        if nodeinfo:
            # 루트 노드 정보 찾기 (3분할 과정. 각 순회에서 루트, 좌측 서브트리, 우측 서브트리 탐색)
            # x 좌표 기준으로 정렬된 nodeinfo 에서 index, y, 노드번호
            root = (0,-1,0)
            for idx, (x,y,n) in enumerate(nodeinfo):
                # 특정 순회에서 y 값이 가장 큰 루트 노드 찾기
                if y > root[1]:
                    root = (idx, y, n)

            # 좌측 서브트리, 우측 서브트리
            left_sub, right_sub = nodeinfo[:root[0]], nodeinfo[root[0]+1:]
            
            # 좌, 우 서브트리 탐색 전 루트노드 출력 -> 전위 순회
            result[0].append(root[-1])
            # 좌측 서브트리 탐색
            make_order(left_sub)
            # 좌측 서브트리 탐색 후 루트노드 출력, 우측 서브트리 탐색 -> 중위 순회
            #result[2].append(root[-1])
            # 우측 서브트리 탐색
            make_order(right_sub)
            # 좌, 우 서브트리 탐색 후 루트노드 출력 -> 후위 순회
            result[1].append(root[-1])
    
    make_order(nodeinfo)
    return result