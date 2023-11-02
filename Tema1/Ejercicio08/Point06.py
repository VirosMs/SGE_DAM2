# Initialize the board with empty spaces
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Function to print the board
def print_board():
    print('-------------')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

# Function to check if a move is valid
def is_valid_move(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    elif board[row][col] != ' ':
        return False
    else:
        return True

# Function to check if there is a winner
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    # Check for tie
    for row in board:
        for col in row:
            if col == ' ':
                return None
    return 'tie'

# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        try:
            row = int(input('Enter row (1-3) for ' + player + ': ')) - 1
            col = int(input('Enter column (1-3) for ' + player + ': ')) - 1
        except ValueError:
            print('Invalid input. Try again.')
            continue
        if is_valid_move(row, col):
            board[row][col] = player
            winner = check_winner()
            if winner:
                print_board()
                if winner == 'tie':
                    print('It is a tie!')
                else:
                    print('Player ' + winner + ' wins!')
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('Invalid move. Try again.')

# Start the game
play_game()
