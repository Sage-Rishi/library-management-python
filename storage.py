import json
from models import *

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load_books(self):
        try:
            with open(self.filename, 'r+') as file:
                books_data = json.load(file)
                return [Book(book["title"], book["author"], book["isbn"]) for book in books_data]
        except FileNotFoundError:
            return []

    def save_book(self, books):
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in books], file, indent=4)
    
    def load_users(self):
        try:
            with open(self.filename, 'r+') as file:
                users_data = json.load(file)
                return [User(user["name"], user["user_id"]) for user in users_data]
        except FileNotFoundError:
            return []
    
    def save_user(self, users):
        with open(self.filename, 'w') as file:
            json.dump([user.to_dict() for user in users], file, indent=4)
    
    def load_checkouts(self):
        try:
            with open(self.filename, 'r+') as file:
                checkouts_data = json.load(file)
                return [Checkout(checkout["user_id"], checkout["isbn"], checkout["check_in_date"], checkout["check_out_date"]) for checkout in checkouts_data]
        except FileNotFoundError:
            return []
    
    def save_checkout(self, checkouts):
        with open(self.filename, 'w') as file:
            json.dump([checkout.to_dict() for checkout in checkouts], file, indent=4)