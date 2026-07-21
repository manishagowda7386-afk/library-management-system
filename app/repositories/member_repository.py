from app.utils.json_handler import JsonHandler


class MemberRepository:
    FILE_PATH = "data/members.json"

    def __init__(self):
        self.members = JsonHandler.load_data(self.FILE_PATH)

    def add_member(self, member):
        self.members.append(member.__dict__)
        JsonHandler.save_data(self.FILE_PATH, self.members)

    def get_all_members(self):
        return self.members

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member["member_id"] == member_id:
                return member
        return None

    def remove_member(self, member_id):
        for member in self.members:
            if member["member_id"] == member_id:
                self.members.remove(member)
                JsonHandler.save_data(self.FILE_PATH, self.members)
                return True
        return False