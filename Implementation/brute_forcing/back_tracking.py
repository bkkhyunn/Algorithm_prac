# back tracking 함수 원형 -> DFS/재귀로 많이 구현한다.
'''
def 백트래킹(n):
    if 정답이면 :
        출력 or 저장
    else :
        for 모든 자식 노드에 대해서:
            if 유망조건(m) :
                자식노드로 이동
                백트래킹(n+1)
                부모노드로 이동
def 유망조건(m):
    if 조건에 안맞으면 :
       return False
    return True
'''

# n-Queens
def is_safe(board, row, col, n):
    '''
    현재 위치에 퀸을 놓아도 안전한지 확인하는 함수.
    즉, 같은 행의 왼쪽, 왼쪽 위 대각선, 왼쪽 아래 대각선을 검사한다.
    '''
    # 같은 행 왼쪽
    for i in range(col):
        if board[row][i] == 1:
            return False

    # 왼쪽 위 대각선
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 왼쪽 아래 대각선
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    '''
    1. 재귀적으로 퀸을 배치한다.
    2. 모든 열에 대해 퀸을 배치할 수 있는지 확인하고, 가능하면 배치하고 다음 열로 넘어간다.
    3. 만약 어떤 배치가 불가능하면, 그 배치를 취소하고 다른 배치를 시도한다.
    '''
    # 모든 퀸이 배치되었을 경우 리턴
    if col >= n:
        return True

    # 함수가 진행되는 열에서 행을 한칸씩 옮기면서 퀸을 배치할 수 있는지 확인
    for i in range(n):
        if is_safe(board, i, col, n):
            # board[i][col] 에 퀸 배치
            board[i][col] = 1

            # board[i][col] 에 배치한 후 다음 열로 넘어간다.
            if solve_n_queens_util(board, col + 1, n):
                return True

            # board[i][col] 배치가 True 가 아니면, 즉 최적해가 아니면 배치하지 않은 것으로 한다.
            board[i][col] = 0

    # 해당 열에서 어느 행에도 퀸을 배치할 수 없으면 False 리턴
    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    # Print the solution
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    return True

# Example
n = 4
solve_n_queens(n)