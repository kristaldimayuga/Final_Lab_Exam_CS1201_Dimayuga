import os
import random
from datetime import datetime
from utils.score import Score

class DiceGame:
    def __init__(self):
        self.final_user_score = 0
        self.final_stagewins = 0
        self.tie_breaker_rounds = 0

    def play_game(self, user):
        current_stage = 1

        while True:
            user_score = 0
            pc_score = 0
            record = Score()
            round_score = 0
            date = datetime.now().strftime("%Y-%m-%d")

            print(f"\n★ Stage {current_stage} ★")
            for round_count in range(1, 4):
                print(f'\n★ Round {round_count}! ★')

                user_dice = random.randint(1, 6)
                pc_dice = random.randint(1, 6)

                print(f'{user.username} rolled {user_dice}')
                print(f'The computer rolled {pc_dice}')

                if user_dice > pc_dice:
                    print(f'{user.username} wins the round!')
                    user_score += 1
                elif user_dice < pc_dice:
                    print(f'The computer wins the round!')
                    pc_score += 1
                else:
                    print("\nIt's a tie!")
                    self.tie_breaker_rounds += 1
                    tie_winner = self.tie_breaker(user)
                    if tie_winner == user:
                        print(f'{user.username} wins the tiebreaker round!')
                        user_score += 1
                    else:
                        print("The computer wins the tiebreaker round!")
                        pc_score += 1

                if round_score >=3:
                    break
            
            self.final_user_score += user_score

            if user_score > pc_score:
                self.final_stagewins += 1
                self.final_user_score += 3

                print(f"\n✿ {user.username} won the stage! ✿")
                print(f'score: {self.final_user_score}')
                print(f'stage wins: {self.final_stagewins}')

                try:
                    next_stage = input("Do you wish to continue to the next stage? (y/n): ")
                    if next_stage.lower() == 'n':
                        self.menu(user)
                        break
                    elif next_stage.lower() == 'y':
                        current_stage +=1
                        continue
                except ValueError as e:
                    print (e)
            elif user_score < pc_score:
                print(f"\n✿ Game over {user.username}! ✿")
                print(f'score: {self.final_user_score}')
                print(f'stage wins: {self.final_stagewins}')
                
            record.save_scores(user.username, self.final_user_score, self.final_stagewins, date)
            self.final_user_score = 0
            self.final_stagewins = 0 
            self.menu(user)

    def tie_breaker(self, user):
        user_dice = random.randint(1, 6)
        pc_dice = random.randint(1, 6)

        print(f'{user.username} rolled {user_dice} for the tiebreaker')
        print(f'The computer rolled {pc_dice} for the tiebreaker')

        if user_dice > pc_dice:
            return user
        elif user_dice < pc_dice:
            return "computer"
        else:
            print("\nTie in the tiebreaker round! Re-rolling...")
            return self.tie_breaker(user)

    def show_topscores(self, user):
        show = Score()
        topscores = show.load_scores()
        
        if topscores:
            topscores.sort(key=lambda x: int(x[1]), reverse=True)
            print("""
   __   __   __   __   ___          ___       __   ___  __   __   __        __   __  
  /__` /  ` /  \ |__) |__     |    |__   /\  |  \ |__  |__) |__) /  \  /\  |__) |  \ 
  .__/ \__, \__/ |  \ |___    |___ |___ /~~\ |__/ |___ |  \ |__) \__/ /~~\ |  \ |__/ 
                                                                                    """)
            for i, (username, f_score, f_wins, date) in enumerate(topscores[:10], 1):
                print(f"{i}. {username}      ✧     Score: {f_score}    ✧     Stage Won: {f_wins}     ✧     Date: {date}")
        
        while True:
            try:
                next_stage = input("\nback to game menu? (yes/no): ")
                if next_stage.lower() == 'yes':
                    self.menu(user)
                elif next_stage.lower() == 'no':
                    self.show_topscores(user)
            except ValueError as e:
                print (e)

    def logout(self):
        from main import Main
        main = Main()
        main.main()

    def menu(self, user):
        while True:
            print(
                """
____ ____ _  _ ___  ____ _  _    ___  _ ____ ____    ____ ____ _  _ ____ 
|__/ |__| |\ | |  \ |  | |\/|    |  \ | |    |___    | __ |__| |\/| |___ 
|  \ |  | | \| |__/ |__| |  |    |__/ | |___ |___    |__] |  | |  | |___                                                                          
"""
            )
            print(f"Welcome {user.username}")
            print("1. Start")
            print("2. Top Scores")
            print("3. Logout")

            choice = input("Enter your choice: ")
            try:
                if choice == '1':
                    self.play_game(user)
                elif choice == '2':
                    self.show_topscores(user)
                elif choice == '3':
                    self.logout()
                    break
                else:
                    print("Enter a number between 1-3")
            except ValueError:
                print("Please enter a valid number")
