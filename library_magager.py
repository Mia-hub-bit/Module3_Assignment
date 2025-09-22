from book import Book

def add_book(library: list[Book]):
    """
    Prompts the user for book details, creates a new Book object, and adds it to the library.

    Args:
        library (list[Book]): The list to which the new book will be added.
    """
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    new_book = Book(title, author, isbn)
    library.append(new_book)
    print(f"Book '{title}' added to the library.")

def list_books(library: list[Book]):
    """
    Prints the details of all books in the library.

    Args:
        library (list[Book]): The list of Book objects to print.
    """
    if not library:
        print("The library is currently empty.")
        return
    
    print("\n--- Current Library Collection ---")
    for book in library:
        print(book)
    print("----------------------------------\n")

def find_book(library: list[Book], query: str) -> Book | None:
    """
    Searches the library for a book by title or author.

    Args:
        library (list[Book]): The list of Book objects to search.
        query (str): The search query (title or author).

    Returns:
        Book: The found Book object, or None if no match is found.
    """
    for book in library:
        if query.lower() in book.title.lower() or query.lower() in book.author.lower():
            return book
    return None

def main():
    """
    Main function to run the library management system.
    """
    my_library = []
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(my_library)
        elif choice == '2':
            list_books(my_library)
        elif choice == '3':
            query = input("Enter the title or author to search: ")
            found_book = find_book(my_library, query)
            if found_book:
                print("\nBook found:")
                print(found_book)
            else:
                print("No matching book found.")
        elif choice == '4':
            print("Exiting the program. See Ya!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()