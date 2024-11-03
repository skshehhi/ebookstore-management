class Catalog:
    """
    Represents a catalog containing a collection of e-books.
    """

    def __init__(self):
        # Initialize an empty list of e-books in the catalog
        self._ebooks = []

    # Add an e-book to the catalog
    def add_ebook(self, ebook):
        """Adds an e-book to the catalog."""
        self._ebooks.append(ebook)

    # Remove an e-book from the catalog if it exists
    def remove_ebook(self, ebook):
        """Removes an e-book from the catalog if it exists."""
        if ebook in self._ebooks:
            self._ebooks.remove(ebook)

    # Search for an e-book by title in the catalog
    def search_ebook(self, title):
        """Searches for an e-book by title."""
        for ebook in self._ebooks:
            if ebook.get_title() == title:
                return ebook
        return None

    # String representation of the catalog showing all e-books
    def __str__(self):
        return "Catalog:\n" + "\n".join([str(ebook) for ebook in self._ebooks])
