import os
from board import Board
from player import Player
from menu import Menu

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "2":
            self.quit_game()
        else:
            self.setup_players()
            self.play_game()


    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f"Setting up Player {index}")
            player.choose_name()
            if index == 1:
                player.choose_symbol()
            else:
                # Ensure the second player picks a different symbol
                while True:
                    symbol = input(f"{player.name}, choose your symbol (X or O): ").strip().upper()
                    if symbol in ['X', 'O'] and symbol != self.players[0].symbol:
                        player.symbol = symbol
                        break
                    else:
                        print(f"Invalid symbol. Please choose the other symbol (not '{self.players[0].symbol}').")
            print(f"Player {index} - Name: {player.name}, Symbol: {player.symbol}")
            clear_screen()
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]
        for combo in win_combinations:
            a, b, c = combo
            if self.board.board[a] == self.board.board[b] == self.board.board[c] and self.board.board[a] in ['X', 'O']:
                print(f"{self.players[(self.current_player_index - 1) % 2].name} wins!")
                return True
        return False
    
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = input("Choose a cell (1-9): ").strip()
                cell_num = int(cell_choice)  # Convert to int
                if 1 <= cell_num <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 9 that is not already taken.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        self.switch_player()


    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2


    def quit_game(self):
        print("Thank you for playing! Goodbye!")
        exit()
    

game = Game()
game.start_game()