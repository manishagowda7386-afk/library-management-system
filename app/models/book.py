class Book:
    def __init__(
        self,
        book_id,
        title,
        author,
        isbn,
        category,
        publication_year,
        total_copies,
        available_copies,
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = available_copies
