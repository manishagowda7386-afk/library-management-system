from app.models.book import Book
from app.models.member import Member
from app.models.loan import Loan


class LibraryService:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def issue_book(self, loan):
        self.loans.append(loan)

    def get_all_books(self):
        return self.books

    def get_all_members(self):
        return self.members

    def get_all_loans(self):
        return self.loans
