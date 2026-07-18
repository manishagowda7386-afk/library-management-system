from app.repositories.member_repository import MemberRepository


class MemberService:
    def __init__(self):
        self.member_repository = MemberRepository()

    def add_member(self, member):
        self.member_repository.add_member(member)

    def get_all_members(self):
        return self.member_repository.get_all_members()

    def find_member_by_id(self, member_id):
        return self.member_repository.find_member_by_id(member_id)

    def remove_member(self, member_id):
        return self.member_repository.remove_member(member_id)

    def update_member(self, member_id, updated_member):
        return self.member_repository.update_member(member_id, updated_member)