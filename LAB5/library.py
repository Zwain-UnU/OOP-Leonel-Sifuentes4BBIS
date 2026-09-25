class Library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_users(self, user):
        self.users.append(user)

    def add_books(self, book):
        self.books.append(book)

    def show_list_books(self):
        for book in self.books:
            print(book.show_book_info())
            
