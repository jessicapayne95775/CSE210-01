#Assignment: Week 1 Tic Tac Toe
#Author: Jessica Payne

def display_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print("-+-+-")
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print("-+-+-")
    print(f'{board[6]}|{board[7]}|{board[8]}')

    
def win_board(board):
    return (board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6] or
            board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8])


def player_turn(board):
    x_turn = 0
    
    while x_turn <= 4 and not win_board(board):
        x_placement = int(input("\nX's turn to choose a square (1-9): "))
        if x_placement in board:
            x_location = board.index(x_placement)
            board[x_location] = 'x'
            x_turn += 1
            display_board(board)
            if win_board(board):
                print("\nX Player has won!")

        if not win_board(board):
            o_placement = int(input("\nO's turn to choose a square (1-9): "))
            o_location = board.index(o_placement)
            board[o_location] = 'o'
            display_board(board)
            if win_board(board):
                print("\nO Player has won!")
        if x_turn == 4 and not win_board(board):
            print("It's a draw!")
    print("\nGood game. Thanks for playing!\n")
    

def main(board):
    display_board(board)
    player_turn(board)

board = [1,2,3,4,5,6,7,8,9]
main(board)