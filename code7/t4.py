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
        self.__filesize = filesize  # приватный атрибут с двойным подчёркиванием

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")
        print(f"File size: {self.__filesize} MB")

    def get_filesize(self):
        return self.__filesize

    def set_filesize(self, size):
        if size > 0:
            self.__filesize = size
        else:
            print("File size must be positive")

my_ebook = EBook("1984", "George Orwell", 328, 2)
my_ebook.display()
print("Current filesize:", my_ebook.get_filesize())
my_ebook.set_filesize(3)
print("Updated filesize:", my_ebook.get_filesize())