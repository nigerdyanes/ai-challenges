class Book:
    __num = 0
    __borrowed = 0

    def __init__(self, title, author, isbn, available_quantity, borrowed_quantity):
        self.title = title
        self.author = author
        self.ISBN = isbn
        self.available_quantity = available_quantity
        self.borrowed_quantity = borrowed_quantity
        Book.__num += 1


    @classmethod
    def num_books(cls):
        return cls.__num
    
    @property
    def available(self):
        return self.available_quantity > 0

    @available.setter
    def available(self, quantity):
        self.available_quantity = quantity

    @classmethod
    def borrowed_books(cls):
        return cls.__borrowed
    
    @staticmethod
    def _validate_isbn(isbn):
        return len(isbn) >= 13 and isbn.isdigit()
    
    def __str__(self):
        return f"Book title ${self.title} author {self.author} ISBN {self.ISBN}"
    
    def __del__(self):
        return f"Book destroy: title {self.title}, author {self.author}, ISBN {self.ISBN}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def lend_book(self, quantity):
        if self.available_quantity > quantity:
            self.available_quantity -= quantity
            self.borrowed_quantity +=quantity
        else:
            print("Don't this quanity availible now.")

    def return_book(self, quantity):
        if quantity <= self.borrowed_quantity:
            self.available_quantity += quantity
            self.borrowed_quantity -= quantity
        else:
            print("Invalid quantity to return.")

libro1 = Book("Python for Beginners", "John Smith", "978-1-23456-789-0", 10, 2)

print(libro1.available)  # Salida: True
libro1.available = 0
print(libro1.available)  # Salida: False