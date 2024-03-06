from storage import Storage
from models import User

class Members:
    def __init__(self):
        self.storage = Storage("users.json")
        self.users = self.storage.load_users()
    
    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.storage.save_user(self.users)
    
    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None