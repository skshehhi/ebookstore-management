class Payment:
    """
    Represents payment processing for an order.
    """

    def __init__(self, payment_method, amount):
        # Initialize payment details
        self._payment_method = payment_method
        self._amount = amount
        self._status = "Pending"

    # Process the payment and set the status to completed
    def process_payment(self):
        """Processes the payment and sets the status."""
        self._status = "Completed"

    # Verify if the payment is completed
    def verify_status(self):
        """Returns True if payment is completed."""
        return self._status == "Completed"

    # String representation of the payment showing method, amount, and status
    def __str__(self):
        return f"Payment(method={self._payment_method}, amount={self._amount}, status={self._status})"

