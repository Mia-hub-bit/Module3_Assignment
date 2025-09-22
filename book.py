class Book:
    """
    A class to represent a book with a title, author, and ISBN.
    """
    def __init__(self, title: str, author: str, isbn: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the book.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def get_details(self) -> dict:
        """
        Returns a dictionary containing the book's details.
        """
        return {"title": self.title, "author": self.author, "isbn": self.isbn}