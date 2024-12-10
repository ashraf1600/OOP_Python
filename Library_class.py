#-------------------------------------------------------------------------------------------------------
class Library:
    book_list = []

    def entry_book(self, book):
        if isinstance(book, Book):
            self.book_list.append(book)
            print(f"'{book.title}' is added to the library.")
        else:
            print("Only objects of type 'Book' can be added.")

    def display_books(self):
        if not self.book_list:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.book_list:
                print(f"ID: {book.book_id}, Title: '{book.title}', "
                      f"Author: {book.author}, Available: {'Yes' if book.availability else 'No'}")
 #-------------------------------------------------------------------------------------------------------               
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self)
#============================================================================================================
if __name__ == "__main__":
    book1 = Book(1, "1984", "George Orwell", True)
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", False)
    library = Library()
    library.entry_book(book1)
    library.entry_book(book2)
    library.display_books()
