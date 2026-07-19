from app.repositories.book_repository import BookRepository


class LibraryService:
    def __init__(self):
        self.book_repository = BookRepository()

    def add_book(self, book):
        self.book_repository.add_book(book)

    def get_all_books(self):
        return self.book_repository.get_all_books()

    def find_book_by_id(self, book_id):
        return self.book_repository.find_book_by_id(book_id)

    def remove_book(self, book_id):
        return self.book_repository.remove_book(book_id)
        