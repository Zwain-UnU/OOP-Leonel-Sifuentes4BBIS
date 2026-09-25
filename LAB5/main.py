from books import Book
from users import User
from library import Library

book1 = Book("001", "OOP FUNDAMENTALS", "Jhon L",  "BBC")
book2 = Book("002", "Python for dummies", "Stef Maruzh", "For Dummies")

user1 = User("001", "Leonel", "Leonel-1234")

library = Library()

library.add_books(book1)
library.add_books(book2)

library.add_users(user1)
library.show_list_books()

"""
Requeriments
1.- The system must allow register Books.
2.- The system must allow register Users.
3.- The system must allow a book to be borrowed by a user.
4.- A book that has already been borrowed cannot be borrowed again.
5.- The system must allow a book to be returned.
"""