from book import Book
from membership import Membership
class Member(Membership):
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = [Book]
        self.badge = ''

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}"

    def update_email(self, new_email):
        self.email = new_email
        print(f"Email updated to: {self.email}")

    def get_details(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email
        }
    
    def member_book_details(self):
        for book in self.borrowed_books:
            if isinstance(book, Book):
                print(f"Subscription: {self.badge} -- Member {self.name} (ID: {self.member_id}) has the book: {book.title} by {book.author} (ISBN: {book.isbn})")
            else:
                print(f"Subscription: {self.badge} -- Member {self.name} (ID: {self.member_id}) has no valid book details.")

    def add_badge(self, badge):
        if (badge in super().badges and badge != self.badge):
            self.badge = badge
            print(f"Badge '{badge}' added to member {self.name} (ID: {self.member_id}).")
        else:
            print(f"Badge '{badge}' is invalid.")