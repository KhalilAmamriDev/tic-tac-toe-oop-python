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
        current_player_index = 0
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "2":
            self.quit_game()
        else:
            self.setup_players()
            self.play_game()

    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            player.choose_name()
            player.choose_symbol()
            print(f"Player {index} - Name: {player.name}, Symbol: {player.symbol}")
            print("-" * 20)
    def play_game(self):
        #while True:
            pass
    def quit_game(self):
        pass
    
game = Game()
game.start_game()
