class Membership():

    badges = ['Gold', 'Silver', 'Bronze']
    
    def __init__(self, member_id):
        self.member_id = member_id
        self.members = {}

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' added with ID: {member.member_id}")
    