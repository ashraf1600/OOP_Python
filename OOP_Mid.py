class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__availability

    def borrow_book(self):
        if self.__availability:
            print(f"'{self.__title}' is available! Borrowing now.")
            self.__availability = False
        else:
            print(f"'{self.__title}' is currently not available for borrowing.")

    def return_book(self):
        if not self.__availability:
            print(f"'{self.__title}' has been returned and is now available.")
            self.__availability = True
        else:
            print(f"'{self.__title}' was not borrowed, so it cannot be returned.")

    def view_book_info(self):
        availability_status = "Yes" if self.__availability else "No"
        print(f"Book ID: {self.__book_id}\n"
              f"Title: '{self.__title}'\n"
              f"Author: {self.__author}\n"
              f"Available: {availability_status}")

class Library:
    def __init__(self):
        self._book_list = []

    def entry_book(self, book):
        if isinstance(book, Book):
            self._book_list.append(book)
            print(f"'{book.get_title()}' is added to the library.")
        else:
            print("Only valid Book objects can be added.")

    def display_books(self):
        if not self._book_list:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for book in self._book_list:
                print(f"ID: {book.get_book_id()}, Title: '{book.get_title()}', "
                      f"Author: {book.get_author()}, Available: {'Yes' if book.is_available() else 'No'}")

    @property
    def book_list(self):
        return self._book_list

def menu():
    library = Library()
    library.entry_book(Book(1, "Bangladesh: A Legacy Of Blood", "Anthony Mascarenhas", True))
    library.entry_book(Book(2, "Amar fashi Chai", "Motiur Rahman Rentu", True))
    library.entry_book(Book(3, "Kothau Keu Nei", "Humayun Ahmed", True))
    library.entry_book(Book(4, "Amar dekha July'24", "Ashraful Islam", False))
    library.entry_book(Book(5, "C Programming", "Subeen", True))
    library.entry_book(Book(6, "Data Structure", "Schaums", True))
    library.entry_book(Book(7, "Shopno jabe bari Amar", "Ashraful Islam", False))
    library.entry_book(Book(8, "Lucky bashkar", "IDK", False))

    while True:
        print("\nLibrary Management System")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            try:
                book_id = int(input("Enter the Book ID to borrow: "))
                book_found = False
                for book in library.book_list:
                    if book.get_book_id() == book_id:
                        book.borrow_book()
                        book_found = True
                        break
                if not book_found:
                    print(f"Book with ID {book_id} does not exist.")
            except ValueError:
                print("Invalid input. Please enter a valid Book ID.")
        elif choice == "3":
            try:
                book_id = int(input("Enter the Book ID to return: "))
                book_found = False
                for book in library.book_list:
                    if book.get_book_id() == book_id:
                        book.return_book()
                        book_found = True
                        break
                if not book_found:
                    print(f"Book with ID {book_id} does not exist.")
            except ValueError:
                print("Invalid input. Please enter a valid Book ID.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("____________________Welcome To the Library____________________\n")
    menu()
