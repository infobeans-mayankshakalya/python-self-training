from book import Book
from comicBook import ComicBook
from library import Library
from member import Member

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

member1 = Member(1, "Mayank", "mshakalya@test.com")
member2 = Member(2, "Rahul", "rahul@test.com")

member1.add_badge("Gold")
member2.add_badge("Silver")

library = Library()

library.manage_membership(member1)
library.manage_membership(member2)

library.add_book(book1)
library.add_book(book2)
library.list_books()
library.remove_book(book1)
library.list_books()
library.remove_book(book1)  # Attempting to remove a book that is not in the library
library.list_books()
library.add_book(book1)  # Adding the book back to the library
library.list_books()

comic1 = ComicBook("Spider Men", "Stan Lee", "1122334455", "Steve Ditko")
comic2 = ComicBook("Batman", "Bob Kane", "5566778899", "Bill Finger")
library.add_book(comic1)
library.add_book(comic2)
library.list_books()

member1.borrowed_books.append(book1)
member1.member_book_details()
member2.borrowed_books.append(comic1)
member2.borrowed_books.append(comic2)
member2.member_book_details()