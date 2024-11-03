class EBook:
    """
    Represents an e-book with title, author, publication date, genre, and price.
    """

    def __init__(self, title, author, publication_date, genre, price):
        # Initialize e-book details
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # Getter for title
    def get_title(self):
        return self._title

    # Getter for author
    def get_author(self):
        return self._author

    # Getter for publication date
    def get_publication_date(self):
        return self._publication_date

    # Getter for genre
    def get_genre(self):
        return self._genre

    # Getter for price
    def get_price(self):
        return self._price

    # Setter for price
    def set_price(self, price):
        self._price = price

    # String representation of an e-book for easy display
    def __str__(self):
        return f"EBook(title={self._title}, author={self._author}, genre={self._genre}, price={self._price})"

