class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"