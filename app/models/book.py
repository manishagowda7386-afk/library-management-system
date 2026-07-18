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

    def __str__(self):
        return (
            f"{self.book_id} | "
            f"{self.title} | "
            f"{self.author} | "
            f"ISBN: {self.isbn} | "
            f"Category: {self.category} | "
            f"Published: {self.publication_year} | "
            f"Available: {self.available_copies}/{self.total_copies}"
        ) 