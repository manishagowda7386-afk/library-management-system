from app.models.loan import Loan


class LoanService:
    def __init__(self, loan_repository, book_repository, member_repository):
        self.loan_repository = loan_repository
        self.book_repository = book_repository
        self.member_repository = member_repository

    def issue_book(self, member_id, book_id):
        member = self.member_repository.find_member_by_id(member_id)
        if member is None:
            return False, "Member not found."

        book = self.book_repository.find_book_by_id(book_id)
        if book is None:
            return False, "Book not found."

        if book.available_copies <= 0:
            return False, "No copies available."

        for loan in self.loan_repository.get_all_loans():
            if (
                loan.member_id == member_id
                and loan.book_id == book_id
                and not loan.returned
            ):
                return False, "Member already has this book."

        loan = Loan(member_id, book_id)

        self.loan_repository.add_loan(loan)

        book.available_copies -= 1

        return True, "Book issued successfully."

    def return_book(self, member_id, book_id):
        loans = self.loan_repository.get_all_loans()

        for loan in loans:
            if (
                loan.member_id == member_id
                and loan.book_id == book_id
                and not loan.returned
            ):
                loan.returned = True

                book = self.book_repository.find_book_by_id(book_id)
                if book:
                    book.available_copies += 1

                return True, "Book returned successfully."

        return False, "Loan not found."

    def get_active_loans(self):
        active_loans = []

        for loan in self.loan_repository.get_all_loans():
            if not loan.returned:
                active_loans.append(loan)
        return active_loans