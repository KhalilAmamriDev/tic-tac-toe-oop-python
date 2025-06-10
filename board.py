class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
             print("-" * 5)
    def update_board(self, position, symbol):
        if self.is_valid_move(position):
            self.board[int(position) - 1] = symbol
            return True
        else:
            print("Invalid move. Try again.")
            return False
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]
    

    def  is_valid_move(self, position):
        if position.isdigit() and 1 <= int(position) <= 9:
            return self.board[int(position) - 1] not in ['X', 'O']
        return False      
     