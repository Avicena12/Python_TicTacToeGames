import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            else:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("That square is already occupied. Choose another.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    for combination in winning_combinations:
        if all(board[row][col] == sign for row, col in combination):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, col = random.choice(free_fields)
    board[row][col] = "X"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Computer's first move (middle of the board)
    board[1][1] = "X"
    
    display_board(board)
    
    while True:
        enter_move(board)
        display_board(board)
        
        if victory_for(board, "O"):
            print("Congratulations! You win!")
            break
        
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("It's a tie!")
            break
        
        draw_move(board)
        print("Computer's move:")
        display_board(board)
        
        if victory_for(board, "X"):
            print("Computer wins! Try again.")
            break
        
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
