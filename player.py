class Player:
    # Represents a player in the game.
    # Constructor to initialize the player's name and symbol
    def __init__(self):
        self.name = ""
        self.symbol = ""
    def choose_name(self):
        while True:
            name = input("Enter your name: ").strip()
            if name.isalpha() and len(name) > 0:
                self.name = name
                break
            else:
                print("Invalid name. Please enter a valid name containing only letters.")
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (X or O): ").strip().upper()
            if symbol in ['X', 'O']:
                self.symbol = symbol
                break
            else:
                print("Invalid symbol. Please choose either 'X' or 'O'.")
    