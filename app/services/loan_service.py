from app.repositories.loan_repository import LoanRepository


class LoanService:
    def __init__(self):
        self.loan_repository = LoanRepository()

    def add_loan(self, loan):
        self.loan_repository.add_loan(loan)

    def get_all_loans(self):
        return self.loan_repository.get_all_loans()

    def find_loan_by_id(self, loan_id):
        return self.loan_repository.find_loan_by_id(loan_id)

    def remove_loan(self, loan_id):
        return self.loan_repository.remove_loan(loan_id)

    def update_loan(self, loan_id, updated_loan):
        return self.loan_repository.update_loan(loan_id, updated_loan)