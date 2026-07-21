from app.utils.json_handler import JsonHandler


class LoanRepository:
    FILE_PATH = "data/loans.json"

    def __init__(self):
        self.loans = JsonHandler.load_data(self.FILE_PATH)

    def add_loan(self, loan):
        self.loans.append(loan.__dict__)
        JsonHandler.save_data(self.FILE_PATH, self.loans)

    def get_all_loans(self):
        return self.loans

    def find_loan(self, member_id, book_id):
        for loan in self.loans:
            if (
                loan["member_id"] == member_id
                and loan["book_id"] == book_id
                and not loan["returned"]
            ):
                return loan
        return None

    def remove_loan(self, member_id, book_id):
        loan = self.find_loan(member_id, book_id)

        if loan:
            self.loans.remove(loan)
            JsonHandler.save_data(self.FILE_PATH, self.loans)
            return True

        return False

    def update_loans(self):
        JsonHandler.save_data(self.FILE_PATH, self.loans)