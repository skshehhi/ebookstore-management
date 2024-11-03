class Promotion:
    """
    Represents a promotion with a discount rate and eligibility criteria.
    """

    def __init__(self, discount_rate, min_quantity=1, eligibility=False):
        # Initialize promotion details
        self._discount_rate = discount_rate
        self._min_quantity = min_quantity
        self._eligibility = eligibility

    # Apply promotion discount if conditions are met
    def apply_promotion(self, order):
        """Applies promotion discount if conditions are met."""
        if len(order._items) >= self._min_quantity:
            order.apply_discount(self._discount_rate)

    # String representation of the promotion showing discount rate and minimum quantity
    def __str__(self):
        return f"Promotion(discount_rate={self._discount_rate}, min_quantity={self._min_quantity})"
