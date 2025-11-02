class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

class EBook(Book):
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.filesize = filesize

    def display(self):
        super().display()
        print(f"File size: {self.filesize} MB")

my_ebook = EBook("1984", "George Orwell", 328, 2)
my_ebook.display()