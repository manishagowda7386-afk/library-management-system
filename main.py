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
    print("3. Add Member")
    print("4. View Members")
    print("5. Exit")


def add_book():
    print("\nAdd Book")

    book = Book(
        input("Book ID: "),
        input("Title: "),
        input("Author: "),
        input("ISBN: "),
        input("Category: "),
        input("Publication Year: "),
        int(input("Total Copies: ")),
        0,
    )

    book.available_copies = book.total_copies

    library_service.add_book(book)

    print("\nBook added successfully.")


def view_books():
    books = library_service.get_all_books()

    if not books:
        print("\nNo books found.")
        return

    print("\n========== Books ==========")

    for book in books:
        print(book)


def add_member():
    print("\nAdd Member")

    member = Member(
        input("Member ID: "),
        input("Name: "),
        input("Email: "),
        input("Phone: "),
    )

    member_service.add_member(member)

    print("\nMember added successfully.")


def view_members():
    members = member_service.get_all_members()

    if not members:
        print("\nNo members found.")
        return

    print("\n========== Members ==========")

    for member in members:
        print(member)


while True:
    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        add_member()

    elif choice == "4":
        view_members()

    elif choice == "5":
        print("\nThank you for using Library Management System.")
        break

    else:
        print("\nInvalid choice.")
