class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


book1 = Book("title1", "author1")
book2 = Book("title2", "author2")
book3 = Book("title3", "author3")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book in library.get_books():
    print(book)
