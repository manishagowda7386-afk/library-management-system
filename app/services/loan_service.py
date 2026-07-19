from app.repositories.loan_repository import LoanRepository
from app.models.loan import Loan


class LoanService:
    def __init__(self):
        self.loan_repository = LoanRepository()

    def issue_book(
        self,
        loan_id,
        book,
        member,
        issue_date,
        due_date,
    ):
        if book.available_copies <= 0:
            return False

        loan = Loan(
            loan_id,
            book.book_id,
            member.member_id,
            issue_date,
            due_date,
        )

        self.loan_repository.add_loan(loan)

        book.available_copies -= 1

        return True

    def return_book(self, loan_id, book):
        loan = self.loan_repository.find_loan_by_id(loan_id)

        if loan is None:
            return False

        if loan.returned:
            return False

        loan.returned = True
        book.available_copies += 1

        return True

    def get_all_loans(self):
        return self.loan_repository.get_all_loans()

    def find_loan_by_id(self, loan_id):
        return self.loan_repository.find_loan_by_id(loan_id)