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

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "category": self.category,
            "publication_year": self.publication_year,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["isbn"],
            data["category"],
            data["publication_year"],
            data["total_copies"],
            data["available_copies"],
        )

    def __str__(self):
        return (
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Available: {self.available_copies}/{self.total_copies}"
        )