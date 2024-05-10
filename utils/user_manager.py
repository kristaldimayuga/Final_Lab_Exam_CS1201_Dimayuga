import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.users_path = "data/users.txt"
    
    def load_user(self):
        if not os.path.exist(self.users_path):
            return
        
        with open(self.users_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                self.users.append(User(username, password))

    def save_users(self):
        with open(self.users_path, 'w') as file:
            for user in self.users:
                file.write(f'{user.username} , {user.password}\n')
            
    def validate_username(self,username):
        if len(username) < 4:
            raise ValueError("username must be 4 characters long")

    def validate_password(self,password):
        if len(password) < 8:
            raise ValueError("password must be 8 characters long")

    def register(self):
        print("Register an account")
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                self.validate_username(username)
                self.validate_password(password)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            self.users.append(User(username , password))
            print("Registered successfully!")
            break

    def login(self):
        print("login to your account")
        username=input("Enter username: ")
        password=input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print("log in successful!")
                return user
            else:
                print ("invalid username and password")