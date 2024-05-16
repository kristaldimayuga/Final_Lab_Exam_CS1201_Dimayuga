from utils.user_manager import UserManager
from utils.dice_game import DiceGame

class Main:
    def __init__(self):
        self.user_manager = UserManager()
        self.dice_game = DiceGame()

    def main(self):

        while True:
            print("Random Dice Game")
            print("1. register")
            print("2. login")
            print("3. exit")

            choice = int(input("Enter your choice: "))

            try:
                if choice == 1:
                    self.user_manager.register()
                elif choice == 2:
                    logged_in_user=self.user_manager.login()
                    if logged_in_user:
                        self.dice_game.menu(logged_in_user)
                elif choice == 3:
                    
                else:
                    print("Enter a number between 1-3")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    game = Main()
    game.main()
