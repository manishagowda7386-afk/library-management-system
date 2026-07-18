from app.models.book import Book
from app.models.member import Member
from app.models.loan import Loan
from app.services.library_service import LibraryService


def main():
    library = LibraryService()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
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
            print("Book added successfully!")

        elif choice == "2":
            books = library.get_all_books()

            if not books:
                print("No books available.")
            else:
                print("\nBooks:")
                for book in books:
                    print(
                        f"{book.book_id} | {book.title} | {book.author} | Available: {book.available_copies}/{book.total_copies}"
                    )

        elif choice == "3":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
