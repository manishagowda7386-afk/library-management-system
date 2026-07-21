from app.utils.json_handler import JsonHandler


class BookRepository:
    FILE_PATH = "data/books.json"

    def __init__(self):
        self.books = JsonHandler.load_data(self.FILE_PATH)

    def add_book(self, book):
        self.books.append(book.__dict__)
        JsonHandler.save_data(self.FILE_PATH, self.books)

    def get_all_books(self):
        return self.books

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                return book
        return None

    def remove_book(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                self.books.remove(book)
                JsonHandler.save_data(self.FILE_PATH, self.books)
                return True
        return False
        