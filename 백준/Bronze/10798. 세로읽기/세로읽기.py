board = [list(input()) for _ in range(5)]
max_length = len(max(board, key=lambda x: len(x)))
answer = ''
for j in range(max_length):
    for i in range(5):
        if len(board[i])-1 >= j:
            answer += board[i][j]
            
print(answer)