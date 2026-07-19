class LoanRepository:
    def __init__(self):
        self.loans = []

    def add_loan(self, loan):
        self.loans.append(loan)

    def get_all_loans(self):
        return self.loans

    def find_loan(self, member_id, book_id):
        for loan in self.loans:
            if (
                loan.member_id == member_id
                and loan.book_id == book_id
                and not loan.returned
            ):
                return loan
        return None

    def remove_loan(self, member_id, book_id):
        loan = self.find_loan(member_id, book_id)

        if loan:
            self.loans.remove(loan)
            return True

        return False

    def get_member_loans(self, member_id):
        member_loans = []

        for loan in self.loans:
            if loan.member_id == member_id:
                member_loans.append(loan)

        return member_loans