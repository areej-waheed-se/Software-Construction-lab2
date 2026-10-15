# Library Book Management System

book_records = []

# Add a book to the library
def add_book(book_name, book_quantity):
    book = {
        "name": book_name,
        "quantity": book_quantity
    }
    book_records.append(book)

# Display all book records
def display_books():
    for book in book_records:
        print("Book Name:", book["name"])
        print("Quantity:", book["quantity"])
        print("------------------")

# Add sample books
add_book("Computer Science", 4)
add_book("Web Development", 6)

# Show all books
display_books()