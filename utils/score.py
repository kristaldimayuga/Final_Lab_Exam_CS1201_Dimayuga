import os
from datetime import datetime

class Score:
    def __init__(self):
        self.data_folder = 'data'
        self.scores_file= 'scores.txt'
        self.path= os.path.join(self.data_folder, self.scores_file)

    def load_scores(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                scores = file.readlines()
                scores = [score.strip().split(', ') for score in scores]
                return scores
        else:
            print("No scores recorded yet.")
            return None

    def save_scores(self, username, f_score, f_wins, date):
        if not os.path.exists(self.path):
            os.makedirs(self.data_folder)

        with open(self.path, 'a+') as file:
            file.write(f"{username}, {f_score}, {f_wins}, {date}\n")
