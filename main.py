from app.models.book import Book
from app.models.member import Member
from app.services.library_service import LibraryService
from app.services.member_service import MemberService

library_service = LibraryService()
member_service = MemberService()


def display_menu():
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Add Member")
    print("6. View Members")
    print("7. Exit")


def add_book():
    book = Book(
        input("Book ID: "),
        input("Title: "),
        input("Author: "),
        input("ISBN: "),
        input("Category: "),
        input("Publication Year: "),
        int(input("Total Copies: ")),
        int(input("Available Copies: "))
    )

    library_service.add_book(book)
    print("\nBook added successfully.")


def view_books():
    books = library_service.get_all_books()

    if not books:
        print("\nNo books available.")
        return

    print("\n========== Books ==========")

    for book in books:
        print(book)


def search_book():
    book_id = input("\nEnter Book ID: ")

    book = library_service.find_book_by_id(book_id)

    if book:
        print(book)
    else:
        print("\nBook not found.")


def remove_book():
    book_id = input("\nEnter Book ID: ")

    if library_service.remove_book(book_id):
        print("\nBook removed successfully.")
    else:
        print("\nBook not found.")


def add_member():
    member = Member(
        input("Member ID: "),
        input("Name: "),
        input("Email: "),
        input("Phone: ")
    )

    member_service.add_member(member)

    print("\nMember added successfully.")


def view_members():
    members = member_service.get_all_members()

    if not members:
        print("\nNo members available.")
        return

    print("\n========== Members ==========")

    for member in members:
        print(member)


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            remove_book()

        elif choice == "5":
            add_member()

        elif choice == "6":
            view_members()

        elif choice == "7":
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()