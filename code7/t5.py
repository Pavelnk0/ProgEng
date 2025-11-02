class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

class AudioBook(Book):
    def __init__(self, title, author, length):
        super().__init__(title, author, pages=0)  # страниц нет
        self.length = length  # длительность в минутах

    def display(self):
        print(f"Audiobook: '{self.title}' by {self.author}, length {self.length} minutes")

def show_info(book):
    book.display()

book1 = Book("1984", "George Orwell", 328)
audiobook = AudioBook("1984", "George Orwell", 660)

show_info(book1)
show_info(audiobook)