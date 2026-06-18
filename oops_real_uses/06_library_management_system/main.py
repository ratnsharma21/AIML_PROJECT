class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_issued:
                book.is_issued = True
                return True
        return False

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.is_issued:
                book.is_issued = False
                return True
        return False

    def display_books(self):
        for book in self.books:
            if not book.is_issued:
                print(book.title)

lib = Library()
b1 = Book("Python Basics")
b2 = Book("Design Patterns")
lib.add_book(b1)
lib.add_book(b2)
lib.display_books()
lib.issue_book("Python Basics")
lib.display_books()
lib.return_book("Python Basics")
lib.display_books()
