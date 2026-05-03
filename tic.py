board = [' ']*9
def show():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])
    print()

def win(p):
    
    # if board[0] == p and board[1] == p and board[2] == p:
    #     return True
    # if board[3] == p and board[4] == p and board[5] == p:
    #     return True
    # if board[6] == p and board[7] == p and board[8] == p:
    #     return True
    # if board[0] == p and board[3] == p and board[6] == p:
    #     return True
    # if board[1] == p and board[4] == p and board[7] == p:
    #     return True
    # if board[2] == p and board[5] == p and board[8] == p:
    #     return True
    # if board[0] == p and board[4] == p and board[8] == p:
    #     return True
    # if board[2] == p and board[4] == p and board[6] == p:
    #     return True
    # return False

    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == p for i in line) for line in lines)

while True:
    show()
    pos = int(input('enter position (1-9): ')) - 1
    board[pos] = 'X'

    if win('X'):
        show()
        print('X wins!')
        break

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            break

    if win('O'):
        show()
        print('O wins!')
        break

    if ' ' not in board:
        show()
        print('It\'s a tie!')
        break