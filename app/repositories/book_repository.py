class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)

        if book:
            self.books.remove(book)
            return True

        return False

    def update_book(self, updated_book):
        for index, book in enumerate(self.books):
            if book.book_id == updated_book.book_id:
                self.books[index] = updated_book
                return True

        return False

    def is_book_available(self, book_id):
        book = self.find_book_by_id(book_id)

        if book is None:
            return False

        return book.available_copies > 0
        