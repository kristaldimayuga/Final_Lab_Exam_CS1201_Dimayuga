import os
from datetime import datetime

class Score:
    def __init__(self):
        pass

    def load_scores(self):
        score_file_path = os.path.join('data', 'scores.txt')
        if os.path.exists(score_file_path):
            with open(score_file_path, 'r') as file:
                scores = file.readlines()
                scores = [score.strip().split(', ') for score in scores]
                return scores
        else:
            print("No scores recorded yet.")
            return None

    def save_scores(self, username, score, rounds_won, date):
        score_folder = 'data'
        score_file_path = os.path.join(score_folder, 'scores.txt')

        if not os.path.exists(score_folder):
            os.makedirs(score_folder)

        with open(score_file_path, 'a+') as file:
            file.write(f"{username}, {score}, {rounds_won}, {date}\n")
