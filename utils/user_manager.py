import os
from utils.user import User
from utils.dice_game import DiceGame

class UserManager(User):
    def __init__(self):
        super().__init__("", "", 0)

     
    def validate_username(self):
        if len(self.username) >= 4:
            return True
        else:
            raise ValueError("username must be 4 characters long")

    def validate_password(self):
        if len(self.password) >= 8:
            return True
        else:
            raise ValueError("password must be 8 characters long")

    def register(self):
        print("Register an account")
        user_list = self.load_user()
        
        while True:
            self.username = input("Enter username: ")
            if not self.validate_username():
                continue
            if any(username == self.username for username in self.users):
                print("username already exists.")
                continue

            self.password = input("Enter password: ")
            if not self.validate_password():
                continue
            else:
                self.new_user = User(self.username, self.password, 0)
                user_list.append((self.username, self.password, 0))
                self.save_users(user_list)
                print("You have registered successfully!")
                return
        
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