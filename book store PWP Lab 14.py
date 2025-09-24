class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        print(f"Discount of {percentage}% applied. New price: ₹{self.price:.2f}")

book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("Data Science Essentials", "Jane Doe", 750)

print("Before Discount:")
book1.display_details()
book2.display_details()

print("After Applying Discount on Book 1:")
book1.apply_discount(10)
book1.display_details()

print("Book 2 (no discount):")
book2.display_details()

