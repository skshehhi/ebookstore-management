class Invoice:
    """
    Represents an invoice generated for an order, including VAT and discount details.
    """

    def __init__(self, order):
        # Initialize invoice details from the order
        self._order = order
        self._total_amount = order.calculate_total()
        self._vat = 0.08  # Example VAT rate
        self._discount = 0

    # Generate the final invoice with VAT and discount applied
    def generate_invoice(self):
        """Generates the final invoice with VAT and discount applied."""
        self._total_amount = self._order.calculate_total()
        self._total_amount *= (1 + self._vat) - self._discount

    # String representation of the invoice showing total amount, VAT, and discount
    def __str__(self):
        return f"Invoice(total_amount={self._total_amount}, VAT={self._vat}, discount={self._discount})"

