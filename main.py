from utils.user_manager import UserManager
from utils.dice_game import DiceGame
from utils.user import User

def main():
    user_manager = UserManager()
    dice_game = DiceGame()

    while True:
        print("Random Dice Game")
        print("1. register")
        print("2. login")
        print("3. exit")

        choice = int(input("Enter your choice: "))

        try:
            if choice == 1:
                user_manager.register()
            elif choice == 2:
                logged_in_user=user_manager.login()
                if logged_in_user:
                    dice_game.menu(logged_in_user)
            elif choice == 3:
                break
            else:
                print("Enter a number between 1-3")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
