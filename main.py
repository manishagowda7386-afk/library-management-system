from app.models.book import Book
from app.services.library_service import LibraryService


def display_menu():
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")


def add_book(library):
    print("\nAdd New Book")

    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    category = input("Category: ")
    publication_year = input("Publication Year: ")
    total_copies = int(input("Total Copies: "))

    book = Book(
        book_id,
        title,
        author,
        isbn,
        category,
        publication_year,
        total_copies,
        total_copies,
    )

    library.add_book(book)

    print("\nBook added successfully.")


def view_books(library):
    books = library.get_all_books()

    if not books:
        print("\nNo books available.")
        return

    print("\n========== Books ==========")

    for book in books:
        print(book)


def search_book(library):
    book_id = input("\nEnter Book ID: ")

    book = library.find_book_by_id(book_id)

    if book:
        print("\nBook Found:")
        print(book)
    else:
        print("\nBook not found.")


def remove_book(library):
    book_id = input("\nEnter Book ID to remove: ")

    if library.remove_book(book_id):
        print("\nBook removed successfully.")
    else:
        print("\nBook not found.")


def main():
    library = LibraryService()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book(library)

        elif choice == "2":
            view_books(library)

        elif choice == "3":
            search_book(library)

        elif choice == "4":
            remove_book(library)

        elif choice == "5":
            print("\nThank you for using Library Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()

