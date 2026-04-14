class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False

    def __str__(self):
        status = "read" if self.read else "not read"
        return f"Name: {self.name}\nAuthor: {self.author}\nRelease date: {self.release_date} \nStatus: {status}"


class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        elif isinstance(books, list) and all(isinstance(book, Book) for book in books):
            self.books = books
        else:
            raise TypeError("books must be a list of Book instances or None")

    def __str__(self):
        return f"My books list:\n\n{"\n\n".join(str(book) for book in self.books)}"

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added book: {book.name}")
        else:
            raise TypeError("book must be an instance of Book")

    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.read = True
                return
        print(f"Book named {book_name} not found in the collection")

    def list_books(self):
        if not self.books:
            print("The book collection is empty")
        for book in self.books:
            print(book)


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)


# Create a book collection
my_collection = BookCollection()

# # Add books to the collection
my_collection.add_book(book1)
my_collection.add_book(book2)
my_collection.add_book(book3)

# # List all books
my_collection.list_books()

# # Mark a book as read
my_collection.mark_as_read("1984")

# print(my_collection.books.index("1984"))
# # List books again to see updated status
my_collection.list_books()

# # Try to mark a non-existing book as read
my_collection.mark_as_read("Unknown Book")


print(my_collection)
