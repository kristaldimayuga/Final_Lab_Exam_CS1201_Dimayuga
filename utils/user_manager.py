from utils.user import User

class UserManager:
    def __init__(self):
        self.users=[]

    def load_user(self):
        # Load users from storage (e.g., file/database)
        pass

    def save_users(self):
        # Save users to storage (e.g., file/database)
        pass

    def validate_username(self,username):
        if len(username) < 4:
            raise ValueError("username must be 4 characters long")
            return

        pass

    def validate_password(self,password):
        if len(password) < 8:
            raise ValueError("password must be 8 characters long")
            return
        pass

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
            user = User(username, password)
            self.users.append(user)
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
                
        print ("invalid username and password")

        pass
