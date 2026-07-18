class Member:
    def __init__(
        self,
        member_id,
        first_name,
        last_name,
        email,
        phone,
        address,
        membership_date,
        active=True,
    ):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.membership_date = membership_date
        self.active = active
