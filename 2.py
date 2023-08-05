class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.books.append(book)

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        return results

    def search_by_ISBN(self, ISBN):
        results = [book for book in self.books if ISBN == book.ISBN]
        return results

    def display_books(self):
        print("\nLibrary Catalog:")
        print("=================")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.ISBN}\nStatus: {status}\n")
        print("=================")

class UnibenLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = {}

    def borrow_book(self, title, borrower_name):
        book = next((book for book in self.books if title.lower() == book.title.lower() and book.available), None)
        if book:
            book.available = False
            self.borrowed_books[borrower_name] = book
            return True
        else:
            return False

    def return_book(self, borrower_name):
        if borrower_name in self.borrowed_books:
            book = self.borrowed_books.pop(borrower_name)
            book.available = True
            return True
        else:
            return False

def main():
    print("Welcome to the UNIBEN Library Management System!")
    
    uniben_library = UnibenLibrary("University of Benin Library")
    uniben_library.add_book("Introduction to Engineering", "Michael Smith", "111111")
    uniben_library.add_book("Business and Management", "Laura Johnson", "222222")
    uniben_library.add_book("History of Literature", "Daniel Brown", "333333")

    while True:
        print("\nChoose an option:")
        print("1. Search for a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter the corresponding number: ")

        if choice == "1":
            search_query = input("Enter title or author: ")
            results = uniben_library.search_by_title(search_query) + uniben_library.search_by_author(search_query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.ISBN}")
                print("=================")
            else:
                print("No matching books found.")
        
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            borrower_name = input("Enter your name: ")
            if uniben_library.borrow_book(title, borrower_name):
                print("Book borrowed successfully!")
            else:
                print("Book not available for borrowing.")
        
        elif choice == "3":
            borrower_name = input("Enter your name: ")
            if uniben_library.return_book(borrower_name):
                print("Book returned successfully!")
            else:
                print("Book return not successful or borrower not found.")
        
        elif choice == "4":
            print("Thank you for using the UNIBEN Library Management Software. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
