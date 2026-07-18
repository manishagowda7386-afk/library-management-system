class Member:
    def __init__(
        self,
        member_id,
        name,
        email,
        phone,
    ):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            f"{self.member_id} | "
            f"{self.name} | "
            f"{self.email} | "
            f"{self.phone}"
        )