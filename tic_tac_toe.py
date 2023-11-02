import random

class TTT_cs170_judge:                      # manages Tic-Tac-Toe board & checks the game state
    def __init__(self):                     # initializes empty board
        self.board = []

    def create_board(self, n):              # creates a n x n board
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)

    def display_board(self):                # prints the boards state
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self, player):            # checks if the given player ('X' or 'O') has won
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True

        return False

    def is_board_full(self):                # checks is board is full
        return all([cell in ['X', 'O'] for row in self.board for cell in row])

class Player_1:                             # human player
    def __init__(self, judge):              # initializes with the current board
        self.board = judge.board

    def my_play(self):                      # takes input for the next move
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())
            
            # len(): returns the number of items in a list
            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                self.board[row-1][col-1] = 'X'
                break
            else:
                print("Wrong coordination!")

class Player_2:                             # AI player
    def __init__(self,judge):               # initizalizes with the current board and game judge
        self.judge = judge
        self.board = judge.board
        self.memoization_table = {}         # dictionary to store memoized results

    def is_board_empty(self):               # checks is board is empty
        return all([cell in ['-'] for row in self.board for cell in row])

    def my_play(self):                      # determines the next move using the Minimax algorithm
        boardScore = -1000              
        boardMoveRow = None
        boardMoveColumn = None

        # for each move (empty cell) in the board:
        for i in range(3):
            for j in range (3):
                if (self.board[i][j] == '-'):
                    # make your play to see all the potential outcomes
                    self.board[i][j] = 'O'

                    # call the minimax function to evaluate all potential instances
                    # we're expecting a move that will produce a score of 10
                    # isMax is True if next move belongs to the AI
                    #          False if the next move belongs to the human
                    minimaxScore = self.minimax(self.board, 0, False, -1000, 1000)

                    # undo the play made to discover other options
                    self.board[i][j] = '-'
                        
                    # if currentScore is better than boardScore, reassign boardScore and boardMove
                    if (minimaxScore > boardScore):
                        boardScore = minimaxScore
                        boardMoveRow = i
                        boardMoveColumn = j

        # return the best move for this instance
        self.board[boardMoveRow][boardMoveColumn] = 'O'

    # determines the best move; returns the board's score
    # def minimax(board: List[List[str]], depth: int, maximizing: bool) -> int:
    def minimax(self, board, depth, isMax, alpha, beta):
        # check if this board state is already memoized
        board_hash = hash(tuple(tuple(row) for row in board))
        if board_hash in self.memoization_table:
            return self.memoization_table[board_hash]
        
        # base case:
            # if player 1 (human player) won: -10
            # if player 2 (AI player) won: 10
            # if its a tie: 0
        if self.judge.is_winner('O'):
            score = 10
            #print(score)
            return score
        
        if self.judge.is_winner('X'):
            score = -10
            #print(score)
            return score
        
        if self.judge.is_board_full():
            score = 0
            #print(score)
            return score

        # it's the AI's turn
        if isMax:
            bestScore = -1000

            # for each move (empty cell) in the board:
            for i in range(3):
                for j in range (3):
                    if (board[i][j] == '-'):
                        # make your play to see all the potential outcomes
                        board[i][j] = 'O'

                        # call the minimax function to evaluate all potential board scores
                        # choose the maximum board score
                        # isMax is True if next move belongs to the AI
                        #          False if the next move belongs to the human
                        depth = depth + 1
                        minimaxScore = self.minimax(board, depth, False, alpha, beta)

                        # undo the play made to discover other options
                        board[i][j] = '-'

                        bestScore = max( bestScore, minimaxScore )
                        alpha = max( alpha, bestScore )
                        if beta <= alpha:
                            break
            self.memoization_table[board_hash] = bestScore
            return bestScore

        else:
            bestScore = 1000

            # for each move (empty cell) in the board:
            for i in range(3):
                for j in range (3):
                    if (board[i][j] == '-'):
                        # make your play to see all the potential outcomes
                        board[i][j] = 'X'

                        # call the minimax function to evaluate all potential board scores
                        # choose the maximum board score
                        # isMax is True if next move belongs to the AI
                        #          False if the next move belongs to the human
                        depth = depth + 1
                        minimaxScore = self.minimax(board, depth, True, alpha, beta)

                        # undo the play made to discover other options
                        board[i][j] = '-'

                        bestScore = min( bestScore, minimaxScore )
                        beta = min(beta, bestScore)
                        if beta <= alpha:
                            break
            self.memoization_table[board_hash] = bestScore
            return bestScore

# Main Game Loop
def game_loop():                            # manages the gameplay
    n = 3
    game = TTT_cs170_judge()                # initializes game to the TTT_cs170_judge class
    game.create_board(n)                    # creates a 3 x 3 board
    player1 = Player_1(game)                # initializes player1 to the Player_1 class and the TTT_cs170_judge class
    player2 = Player_2(game)                # initializes player2 to the Player_2 class and the TTT_cs170_judge class
    starter = random.randint(0,1)           # starter = a random integer (0 or 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()                # print board state
        while not win:
            player1.my_play()               # take human player's input for next move
            win = game.is_winner('X')       # checks if human player won
            game.display_board()            # print board state
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():        # checks if board is full
                print("It's a tie!")
                break

            player2.my_play()               # takes AI player's input for next move
            win = game.is_winner('O')       # checks if AI player won
            game.display_board()            # print board state
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

    else:
        print("Player 2 starts.")
        game.display_board()                # print board state
        while not win:
            player2.my_play()               # takes AI player's input for next move
            win = game.is_winner('O')       # checks if AI player won
            game.display_board()            # print board state
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

            player1.my_play()               # take human player's input for next move
            win = game.is_winner('X')       # checks if human player won
            game.display_board()            # print board state
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():        # checks if board is full
                print("It's a tie!")
                break

game_loop()     # uncomment this line to play the game, but it must
                # be commented again when you are submitting the code
