class LoanRepository:
    def __init__(self):
        self.loans = []

    def add_loan(self, loan):
        self.loans.append(loan)

    def get_all_loans(self):
        return self.loans

    def find_loan_by_id(self, loan_id):
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    def remove_loan(self, loan_id):
        loan = self.find_loan_by_id(loan_id)
        if loan:
            self.loans.remove(loan)
            return True
        return False

    def update_loan(self, loan_id, updated_loan):
        for index, loan in enumerate(self.loans):
            if loan.loan_id == loan_id:
                self.loans[index] = updated_loan
                return True
        return False
    