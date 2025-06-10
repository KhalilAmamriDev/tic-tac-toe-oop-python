class Menu:
    def display_main_menu(self):
        print("Welcome to my X O game!")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Please choose an option (1 or 2): ").strip()
        while choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 or 2.")
            choice = input("Please choose an option (1 or 2): ").strip()
        return choice
    def display_endgame_menu(self):
        print("Game Over!")
        print("1. Play Again")
        print("2. Exit")
        choice = input("Please choose an option (1 or 2): ").strip()
        while choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 or 2.")
            choice = input("Please choose an option (1 or 2): ").strip()
        return choice
    
