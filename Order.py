from datetime import datetime

class Order:
    """
    Represents an order containing a list of e-books and pricing details.
    """

    def __init__(self, customer, items):
        # Initialize order details
        self._customer = customer
        self._items = items
        self._order_date = datetime.now()
        self._total_amount = self.calculate_total()

    # Calculate the total amount of the order by summing item prices
    def calculate_total(self):
        """Calculates the total amount for the order."""
        return sum(item.get_price() for item in self._items)

    # Apply a discount to the total amount
    def apply_discount(self, discount_rate):
        """Applies a discount to the total amount."""
        self._total_amount *= (1 - discount_rate)

    # Add VAT to the total amount
    def add_vat(self, vat_rate=0.08):
        """Adds VAT to the total amount."""
        self._total_amount *= (1 + vat_rate)

    # String representation of the order showing customer, total amount, and order date
    def __str__(self):
        return f"Order(customer={self._customer.get_name()}, total_amount={self._total_amount}, order_date={self._order_date})"

