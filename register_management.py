from storage import Storage
from models import *
import time

class Register:
    def __init__ (self):
        self.storage = Storage("register.json")
        self.register = self.storage.load_checkouts()

    def get_item_from_isbn(self, isbn):
        all_books = Storage("books.json").load_books()
        for book in all_books:
            if book.isbn == isbn:
                return book.isbn
        return None
    
    def check_in_book(self, user_id, isbn):
        item_id = self.get_item_from_isbn(isbn)
        if item_id is None:
            print("Book does not exist.")
            return
        last_check_in = max((registry for registry in self.register if registry.isbn == item_id), key=lambda x: x.check_in_date, default=None)
        if last_check_in is not None and last_check_in.check_out_date is None:
            print("Book is already checked in.")
            return
        else:
            check_in_time = time.time()
            new_registry = Checkout(user_id, item_id, check_in_time, None)
            self.register.append(new_registry)
            self.storage.save_checkout(self.register)
    
    def check_out_book(self, user_id, isbn):
        item_id = self.get_item_from_isbn(isbn)
        if item_id is None:
            print("Book does not exist.")
            return
        last_check_in = max((registry for registry in self.register if registry.isbn == item_id and registry.user_id == user_id), key=lambda x: x.check_in_date, default=None)
        if last_check_in is not None and last_check_in.check_out_date is None:
            check_out_date = time.time()
            last_check_in.check_out_date = check_out_date
            for index,registry in enumerate(self.register):
                if registry.isbn == last_check_in.isbn and registry.user_id == last_check_in.user_id and registry.check_in_date == last_check_in.check_in_date:
                    self.register[index] = last_check_in
                    break
            self.storage.save_checkout(self.register)
            print("Book checked out.")
        else:
            print("Book hasn't been checked in by you or does not exist.")
    
    def get_all_checked_in_books(self, user_id):
        checked_in_books = [registry for registry in self.register if registry.check_out_date is None and registry.user_id == user_id]
        all_books = Storage("books.json").load_books()
        for checked_books in checked_in_books:
            for book in all_books:
                if checked_books.isbn == book.isbn:
                    checked_books.title = book.title
                    checked_books.author = book.author
                    checked_books.isbn = book.isbn
        return checked_in_books