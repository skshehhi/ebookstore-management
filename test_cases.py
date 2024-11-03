from EBook import EBook
from Catalog import Catalog
from Customer import Customer
from ShoppingCart import ShoppingCart
from Order import Order
from Invoice import Invoice
from Promotion import Promotion
from Payment import Payment


# Test Case 1: Add, Modify, and Remove E-books in the Catalog
def test_catalog_management():
    catalog = Catalog()

    # Add e-books
    ebook1 = EBook("Book One", "Author A", "2021-01-01", "Fiction", 9.99)
    ebook2 = EBook("Book Two", "Author B", "2022-02-02", "Science", 12.99)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    print("Catalog after adding e-books:")
    print(catalog)

    # Modify an e-book price
    ebook1.set_price(7.99)
    print("\nCatalog after modifying e-book price:")
    print(catalog)

    # Remove an e-book
    catalog.remove_ebook(ebook2)
    print("\nCatalog after removing an e-book:")
    print(catalog)


# Test Case 2: Add, Modify, and Remove Customer Accounts
def test_customer_management():
    # Add a new customer
    customer = Customer("Shatha Khaled", "shatha@example.com", is_loyalty_member=True)
    print("Customer account created:")
    print(customer)

    # Modify customer loyalty status
    customer.set_loyalty_member(False)
    print("\nCustomer after modifying loyalty status:")
    print(customer)


# Test Case 3: Adding E-books to the Shopping Cart
def test_shopping_cart():
    cart = ShoppingCart()
    ebook1 = EBook("Book One", "Author A", "2021-01-01", "Fiction", 9.99)
    ebook2 = EBook("Book Two", "Author B", "2022-02-02", "Science", 12.99)

    # Add e-books to cart
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    print("\nShopping cart after adding e-books:")
    print(cart)

    # Remove an e-book from cart
    cart.remove_item(ebook1)
    print("\nShopping cart after removing an e-book:")
    print(cart)


# Test Case 4: Applying Discounts for Loyalty Members and Bulk Purchases
def test_discounts():
    ebook1 = EBook("Book One", "Author A", "2021-01-01", "Fiction", 9.99)
    ebook2 = EBook("Book Two", "Author B", "2022-02-02", "Science", 12.99)
    ebook3 = EBook("Book Three", "Author C", "2023-03-03", "History", 15.99)
    items = [ebook1, ebook2, ebook3, ebook1, ebook2]  # Adding 5 e-books to qualify for bulk discount

    customer = Customer("Shatha Khaled", "shatha@example.com", is_loyalty_member=True)
    order = Order(customer, items)

    # Apply loyalty discount (10%) and bulk discount (20% for 5+ e-books)
    loyalty_promotion = Promotion(discount_rate=0.1, eligibility=True)
    bulk_promotion = Promotion(discount_rate=0.2, min_quantity=5)

    # Apply both promotions if eligible
    loyalty_promotion.apply_promotion(order)
    bulk_promotion.apply_promotion(order)

    print("\nOrder after applying loyalty and bulk discounts:")
    print(order)


# Test Case 5: Generate Invoice with Discounts and VAT
def test_invoice_generation():
    ebook1 = EBook("Book One", "Author A", "2021-01-01", "Fiction", 9.99)
    ebook2 = EBook("Book Two", "Author B", "2022-02-02", "Science", 12.99)
    items = [ebook1, ebook2]

    customer = Customer("Maryam Saif", "maryam@example.com", is_loyalty_member=True)
    order = Order(customer, items)

    # Apply loyalty discount (10%)
    loyalty_promotion = Promotion(discount_rate=0.1, eligibility=True)
    loyalty_promotion.apply_promotion(order)

    # Generate invoice
    invoice = Invoice(order)
    invoice.generate_invoice()

    print("\nGenerated Invoice:")
    print(invoice)


# Test Case 6: Payment Processing
def test_payment_processing():
    ebook1 = EBook("Book One", "Author A", "2021-01-01", "Fiction", 9.99)
    items = [ebook1]

    customer = Customer("Reem Hamad", "reem@example.com", is_loyalty_member=False)
    order = Order(customer, items)

    # Process payment
    payment = Payment("Credit Card", order.calculate_total())
    payment.process_payment()

    print("\nPayment Details after processing:")
    print(payment)
    print("Payment Status Verified:", payment.verify_status())


# Test Case 7: Update an E-book in the Catalog
def test_update_ebook():
    catalog = Catalog()
    ebook1 = EBook("Original Book", "Original Author", "2020-01-01", "Original Genre", 10.00)
    catalog.add_ebook(ebook1)

    print("\nCatalog after adding original e-book:")
    print(catalog)

    # Update e-book details
    ebook1._title = "Updated Book"
    ebook1._author = "Updated Author"
    ebook1._price = 12.00

    print("\nCatalog after updating e-book details:")
    print(catalog)


# Test Case 8: Modify Customer Contact Information
def test_modify_customer_contact():
    customer = Customer("Shatha Khaled", "oldemail@example.com", is_loyalty_member=False)
    print("\nCustomer before modifying contact information:")
    print(customer)

    # Update customer contact information
    customer._contact_info = "newemail@example.com"

    print("\nCustomer after modifying contact information:")
    print(customer)


# Run all test cases
if __name__ == "__main__":
    print("Testing Catalog Management:")
    test_catalog_management()
    print("\nTesting Customer Management:")
    test_customer_management()
    print("\nTesting Shopping Cart Management:")
    test_shopping_cart()
    print("\nTesting Discount Application:")
    test_discounts()
    print("\nTesting Invoice Generation:")
    test_invoice_generation()
    print("\nTesting Payment Processing:")
    test_payment_processing()
    print("\nTesting E-book Update in Catalog:")
    test_update_ebook()
    print("\nTesting Modify Customer Contact Information:")
    test_modify_customer_contact()
