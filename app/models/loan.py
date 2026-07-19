class Loan:
    def __init__(self, member_id, book_id):
        self.member_id = member_id
        self.book_id = book_id
        self.returned = False

    def __str__(self):
        status = "Returned" if self.returned else "Issued"

        return (
            f"Member ID: {self.member_id} | "
            f"Book ID: {self.book_id} | "
            f"Status: {status}"
        )