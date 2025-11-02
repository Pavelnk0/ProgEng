class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

    def is_long(self):
        return self.pages > 300

my_book = Book("1984", "George Orwell", 328)
my_book.display()
print("Is long book:", my_book.is_long())