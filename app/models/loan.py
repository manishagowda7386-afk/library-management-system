class Loan:
    def __init__(
        self,
        loan_id,
        book_id,
        member_id,
        issue_date,
        due_date,
        return_date=None,
        fine=0.0,
        returned=False,
    ):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine
        self.returned = returned
