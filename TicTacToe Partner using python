
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def game_over(board):
  
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True

  
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    
    for row in board:
        if '-' in row:
            return False

    return True


def evaluate(board):
   
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            if row[0] == 'X':
                return 1
            else:
                return -1

    
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            if board[0][col] == 'X':
                return 1
            else:
                return -1

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        if board[0][0] == 'X':
            return 1
        else:
            return -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        if board[0][2] == 'X':
            return 1
        else:
            return -1

    return 0


def minimax(board, depth, is_maximizing):
    if game_over(board):
        return evaluate(board)

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    best_score = min(score, best_score)
        return best_score


def make_ai_move(board):
    best_score = float('-inf')
    best_row = -1
    best_col = -1

    print("Heuristic Values:")

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '-'

                print("Move: (" + str(i) + ", " + str(j) + ") - Heuristic Value: " + str(score))

                if score > best_score:
                    best_score = score
                    best_row = i
                    best_col = j

    print("Best Move: (" + str(best_row) + ", " + str(best_col) + ")")
    board[best_row][best_col] = 'X'

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


while not game_over(board):
    print_board(board)
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))
    board[row][col] = 'O'
    make_ai_move(board)

print_board(board)
