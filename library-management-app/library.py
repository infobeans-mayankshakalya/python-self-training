from membership import Membership
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(f"- {book}")
    
    def manage_membership(self, member: Membership):
        
        membership = Membership(member.member_id)
        membership.add_member(member)
        print(f"Membership for {member.name} (ID: {member.member_id}) managed successfully.")

    def add_badge(self, badge):
        if badge not in Membership.badges:
            Membership.badges.append(badge)
            print(f"Badge '{badge}' added to the library membership.")
        else:
            print(f"Badge '{badge}' already exists in the library membership.")