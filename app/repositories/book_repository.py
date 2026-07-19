class MemberRepository:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def get_all_members(self):
        return self.members

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def remove_member(self, member_id):
        member = self.find_member_by_id(member_id)

        if member:
            self.members.remove(member)
            return True

        return False

    def update_member(self, updated_member):
        for index, member in enumerate(self.members):
            if member.member_id == updated_member.member_id:
                self.members[index] = updated_member
                return True

        return False

    def member_exists(self, member_id):
        return self.find_member_by_id(member_id) is not None
        