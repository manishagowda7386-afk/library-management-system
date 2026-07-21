class Member:
    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["member_id"],
            data["name"],
            data["email"],
            data["phone"],
        )

    def __str__(self):
        return (
            f"ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Email: {self.email} | "
            f"Phone: {self.phone}"
        )