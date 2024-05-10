import os

class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(username={self.username}, score={self.score})"
    
    def file_load(self, file_path):
        if not os.path.exists(file_path):
            return False
        
        with open(file_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                if self.username == username:
                    self.password = password
                    return True
            return False

    def file_save(self, file_path):
        with open(file_path, 'a') as file:
            file.write(f"{self.username},{self.password}\n")


