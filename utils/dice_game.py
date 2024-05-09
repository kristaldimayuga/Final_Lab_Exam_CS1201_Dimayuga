import random
from datetime import datetime

class DiceGame:
    def __init__(self):
        self.final_user_score = 0
        self.final_stagewins = 0

    def load_scores(self):
        pass

    def save_scores(self):
        pass

    def play_game(self, user):
        while True:
            stage_count=0
            user_score=0
            pc_score=0

            while True:
                stage_count+=1

                print(f"★ Stage {stage_count} ★")
                
                for round_count in range(1,4):
                    print(f'★ Round {round_count}! ★')

                    user_dice = random.randint(1,6)
                    pc_dice = random.randint(1,6)

                    print(f'{user.username} rolled {user_dice}')
                    print(f'The computer rolled {pc_dice}')

                    if user_dice > pc_dice:
                        print(f'{user.username} wins the round!')
                        user_score += 1

                    elif user_dice < pc_dice:
                        print(f'The computer wins the round!')
                        pc_score += 1

                    else:
                        print("It's a tie!")

                print(f"{user.username}'s score for stage {stage_count}: {user_score}")               
                print(f"Computer's score for stage {stage_count}: {pc_score}")
                
                if user_score <=2 :
                    self.final_stagewins +=1
                    user_score +=3
                    print(f"{user.username} won stage {stage_count}!")
                    break
                print(f"Game over, you won a total of {user_score} points and {self.final_stagewins} stages")
                break
            
            self.final_user_score += user_score
            print(f"{user.username}'s final score: {self.final_user_score}")         
        
            if self.final_stagewins != 0:
                next_stage = input("Do you wish to continue the next stage? (yes/no): ")
                if next_stage.lower() == 'no':
                    print(f"Game over, your total score is {self.final_user_score} and {self.final_stagewins} stage wins")
                    break
                else:
                    continue
            else:
                print("Game over!")
                break
        print(f'Game over! {user.username} won {self.final_stagewins} stages and a total of {self.final_user_score} points.')
    
        self.save_scores(self.final_user_score, self.final_stagewins, user.username)
        self.menu(user)

        return self.final_user_score, self.final_stagewins
                              
    def show_topscores(self):
        
        pass

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
                    self.show_topscores()
                elif choice == '3':
                    print("logging out...")
                    return
                else:
                    print("enter a number between 1-3")
            except ValueError:
                print("please enter a number")
        pass
