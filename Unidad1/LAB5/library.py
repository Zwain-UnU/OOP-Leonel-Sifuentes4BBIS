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
            estado = "Disponible" if book.available else "Prestado"
            print(f"{book.show_book_info()} - Estado: {estado}")

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_book(self, book_id):
        for book in self.books:
            if book.id_book == book_id:
                return book
        return None

    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if user == None:
            print(f"Error, No existe el usuario: {user_id}")
            return
        if book == None:
            print(f"Error, No existe el libro titulado: {book_id}")

        if book.available == True:
            book.available = False
            user.borrowed_books.append(book)
            print(f"El libro {book.title} Fue prestado a: {user.name}")
        else:
            print(f"El libro {book.title} ya esta prestado.")

    def return_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if book in user.borrowed_books:
            book.available = True
            user.borrowed_books.remove(book)
            print(f"El usuario {user.name} ha devuelto el libro: {book.title}")
        else:
            print(f"El usuario {user.name} no ha tenido el libro {book.title} en un prestamo")
            
