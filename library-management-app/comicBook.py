from book import Book
class ComicBook(Book):
    def __init__(self, title, author, isbn, illustrator):
        super().__init__(title, author, isbn)
        self.illustrator = illustrator

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Illustrator: {self.illustrator}"

    def __repr__(self):
        return f"ComicBook({self.title!r}, {self.author!r}, {self.isbn!r}, {self.illustrator!r})"
    
    def add_comic(self, comic):
        print(f"Comic '{comic.title}' by {comic.author} added to the collection.")