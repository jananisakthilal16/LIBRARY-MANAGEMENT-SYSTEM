import json  


class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, id, title, author):
        if id in self.books:
            print("⚠️ Book ID already exists.")
        else:
            self.books[id] = Book(id, title, author)
            print(f"✅ Book '{title}' added.")

    def display_books(self):
        if not self.books:
            print("📚 No books in the library.")
            return
        for book in self.books.values():
            status = "Available ✅" if book.available else "Borrowed ❌"
            print(f"{book.id} - {book.title} by {book.author} [{status}]")

    def borrow_book(self, id):
        if id in self.books:
            if self.books[id].available:
                self.books[id].available = False
                print(f"📕 You borrowed '{self.books[id].title}'.")
            else:
                print("⚠️ Book is already borrowed.")
        else:
            print("❌ Book ID not found.")

    def return_book(self, id):
        if id in self.books:
            self.books[id].available = True
            print(f"📗 Book '{self.books[id].title}' returned successfully.")
        else:
            print("❌ Invalid Book ID.")

    def save_to_file(self, filename='library_data.json'):
        try:
            data = {
                id: {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'available': book.available
                } for id, book in self.books.items()
            }
            with open(filename, 'w') as f:
                json.dump(data, f)
            print("💾 Library data saved to file.")
        except Exception as e:
            print("❌ Failed to save:", e)

    def load_from_file(self, filename='library_data.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for id, book_data in data.items():
                    book = Book(
                        book_data['id'],
                        book_data['title'],
                        book_data['author']
                    )
                    book.available = book_data['available']
                    self.books[int(id)] = book
            print("📂 Library data loaded from file.")
        except FileNotFoundError:
            print("⚠️ No saved file found. Starting fresh.")
        except Exception as e:
            print("❌ Failed to load:", e)


lib = Library()
lib.load_from_file()  

while True:
    print("\n====== LIBRARY MENU ======")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        try:
            id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            lib.add_book(id, title, author)
        except ValueError:
            print("❌ Invalid input. ID must be a number.")

    elif choice == '2':
        lib.display_books()

    elif choice == '3':
        try:
            id = int(input("Enter Book ID to borrow: "))
            lib.borrow_book(id)
        except ValueError:
            print("❌ Invalid input. ID must be a number.")

    elif choice == '4':
        try:
            id = int(input("Enter Book ID to return: "))
            lib.return_book(id)
        except ValueError:
            print("❌ Invalid input. ID must be a number.")

    elif choice == '5':
        lib.save_to_file()  # Save data before exiting
        print("👋 Exiting Library System. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter 1 to 5.")
