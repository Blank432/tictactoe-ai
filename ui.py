import logic

board = logic.BOARD_STATE

def change(move):
    return (ord(move[0])-97, int(move[1])-1)

def check_winner(board):
    winner = logic.winner(board)
    if winner != None:
        if winner != 0:
            print(f"{logic.X if winner == 1 else logic.O} won the game!")

        else:
            print("The game ended in a tie!")
    
        return True
    
    else:
        return False

while not logic.terminal(board):
    if check_winner(board):
        break
    
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n"+
           "-|-|-\n"+
          f"{board[1][0]}|{board[1][1]}|{board[1][2]}\n"+
           "-|-|-\n"+
          f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
    move = change(input("It is your turn.\n"))

    if logic.validate_move(board, move):
        board = logic.move(board, move)
    else:
        print("Invalid move!")
        continue
    
    if check_winner(board):
        break

    ai_move = logic.ai(board)
    board = logic.move(board, change(ai_move))