# Global list to store books
from models import Book
from storage import Storage

class Library:
    def __init__(self):
        self.storage = Storage("books.json")
        self.books = self.storage.load_books()
    
    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("Book already exists with similar ISBN. Please enter a different ISBN.")
                return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.storage.save_book(self.books)
        print("Book added.")
    
    def list_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                print(f"Title: {book.title} by {book.author} (ISBN: {book.isbn})")

