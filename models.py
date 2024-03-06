class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

class User:
    def __init__(self, name, user_id):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {"name": self.name, "user_id": self.user_id}

class Checkout:
    def __init__(self, user_id, isbn, check_in_date, check_out_date):
        self.user_id = user_id
        self.isbn = isbn
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def to_dict(self):
        return {"user_id": self.user_id, "isbn": self.isbn, "check_in_date": self.check_in_date, "check_out_date": self.check_out_date}