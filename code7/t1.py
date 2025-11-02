class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: '{self.title}' by {self.author}")

my_book = Book("1984", "George Orwell")
my_book.display()