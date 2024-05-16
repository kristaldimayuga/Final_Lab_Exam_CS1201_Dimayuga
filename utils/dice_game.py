import os
import random
from datetime import datetime
from utils.score import Score

class DiceGame:
    def __init__(self):
        self.final_user_score = 0
        self.final_stagewins = 0
        self.tie_breaker_rounds=0

    def play_game(self, user):
        while True:
            user_score=0
            pc_score=0

            print(f"\n★ stage ★")
            while True:
                for round_count in range(1,4):
                    print(f'\n★ Round {round_count}! ★')

                    user_dice = random.randint(1,6)
                    pc_dice = random.randint(1,6)

                    print(f'\n{user.username} rolled {user_dice}')
                    print(f'The computer rolled {pc_dice}')

                    if user_dice > pc_dice:
                        print(f'\n{user.username} wins the round!')
                        user_score += 1
                    elif user_dice < pc_dice:
                        print(f'\nThe computer wins the round!')
                        pc_score += 1
                    else:
                        print("\nIt's a tie!")
                        self.tie_breaker_rounds +=1
                        tie_winner = self.tie_breaker(user)
                        if tie_winner==user:
                            print(f'\n{user.username} wins the tiebreaker round!')
                            user_score +=1
                        else:
                            print("\nthe computer wins the tiebreaker round!")
                            pc_score +=1

                print(f"\n{user.username}'s score for this stage: {user_score}")               
                print(f"Computer's score for this stage: {pc_score}")

                if user_score >=2 :
                    self.final_stagewins +=1
                    user_score +=3
                    print(f"\n{user.username} won stage!")
                    break
                else:
                    print(f"Game over")
                    self.final_user_score += user_score
                    self.final_stagewins = 0  
                    self.final_user_score = 0  
                    self.menu(user)
                    return

            self.final_user_score += user_score
            print(f"{user.username}'s final score: {self.final_user_score}")
                    
            if self.final_stagewins != 0:
                next_stage = input("Do you wish to continue the next stage? (yes/no): ")
                if next_stage.lower() != 'yes':
                    print(f"Game over, your total score is {self.final_user_score} and {self.final_stagewins} stage wins")
                    self.final_stagewins = 0  
                    self.final_user_score = 0
                    self.menu(user)
                    return
                else:
                    continue

            self.final_user_score += user_score
            print(f"{user.username}'s final score: {self.final_user_score}")

            record = Score()  
            record.save_scores(user.username, self.final_user_score, self.final_stagewins, datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 

            self.final_user_score = 0
            self.final_stagewins = 0

    def tie_breaker(self,user):
        user_dice = random.randint(1, 6)
        pc_dice = random.randint(1, 6)

        print(f'{user.username} rolled {user_dice} for the tiebreaker')
        print(f'The computer rolled {pc_dice} for the tiebreaker')

        if user_dice > pc_dice:
            return user
        elif user_dice < pc_dice:
            return "computer"
        else:
            print("Tie in the tiebreaker round! Re-rolling...")
            return self.tie_breaker(user)
        
    def show_topscores(self, user):
        score_manager = Score()
        scores = score_manager.load_scores()
        if scores:
            user_scores = [score for score in scores if score[0] == user.username] 
            if user_scores:
                os.system('cls')
                print(f"\n{user.username}'s Scores:")
                for i, (_, score, rounds_won, date) in enumerate(user_scores, 1):
                    print(f"{i}. Score: {score}, Rounds Won: {rounds_won}, Date: {date}")       
            else:
                print("No scores recorded for this user.")
        else:
            print("No scores recorded yet.")


    def menu(self,user):
        while True:
            print("Random Dice Game")
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
                    return
                else:
                    print("enter a number between 1-3")
            except ValueError:
                print("please enter a number")
        pass

