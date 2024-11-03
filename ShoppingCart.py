class ShoppingCart:
    """
    Represents a shopping cart containing selected e-books.
    """

    def __init__(self):
        # Initialize an empty list of items in the shopping cart
        self._items = []

    # Add an e-book to the shopping cart
    def add_item(self, ebook):
        """Adds an e-book to the shopping cart."""
        self._items.append(ebook)

    # Remove an e-book from the shopping cart if it exists
    def remove_item(self, ebook):
        """Removes an e-book from the shopping cart if it exists."""
        if ebook in self._items:
            self._items.remove(ebook)

    # Update the quantity of an e-book in the cart (placeholder for quantity logic)
    def update_quantity(self, ebook, qty):
        """Updates the quantity of an e-book in the cart."""
        pass

    # Clear all items in the shopping cart
    def clear_cart(self):
        """Clears all items in the shopping cart."""
        self._items.clear()

    # String representation of the shopping cart showing all items
    def __str__(self):
        return "ShoppingCart:\n" + "\n".join([str(item) for item in self._items])
