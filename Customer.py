class Customer:
    """
    Represents a customer with name, contact information, and loyalty status.
    """

    def __init__(self, name, contact_info, is_loyalty_member=False):
        # Initialize customer details
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member
        self._cart = None  # Placeholder for ShoppingCart instance

    # Getter for name
    def get_name(self):
        return self._name

    # Getter for contact information
    def get_contact_info(self):
        return self._contact_info

    # Check if the customer is a loyalty member
    def is_loyalty_member(self):
        return self._is_loyalty_member

    # Setter for loyalty membership status
    def set_loyalty_member(self, status):
        self._is_loyalty_member = status

    # String representation of the customer for easy display
    def __str__(self):
        return f"Customer(name={self._name}, loyalty_member={self._is_loyalty_member})"

