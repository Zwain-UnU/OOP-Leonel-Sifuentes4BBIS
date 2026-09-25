class Book:
    def __init__(self, id_book, title, author, editorial):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.editorial = editorial
        self.available = True

    def show_book_info(self):
        return f"{self.id_book} - {self.title} - {self.author}"