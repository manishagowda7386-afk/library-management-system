from app.models.book import Book
from app.models.member import Member
from app.services.library_service import LibraryService
from app.services.member_service import MemberService

library_service = LibraryService()
member_service = MemberService()


def menu():
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Add Member")
    print("6. View Members")
    print("7. Exit")


while True:
    menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nAdd Book")

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

    elif choice == "2":
        books = library_service.get_all_books()

        if not books:
            print("\nNo books available.")
        else:
            print("\n========== Books ==========")

            for book in books:
                print(book)

    elif choice == "3":
        book_id = input("\nEnter Book ID: ")

        book = library_service.find_book_by_id(book_id)

        if book:
            print(book)
        else:
            print("\nBook not found.")

    elif choice == "4":
        book_id = input("\nEnter Book ID: ")

        if library_service.remove_book(book_id):
            print("\nBook removed successfully.")
        else:
            print("\nBook not found.")

    elif choice == "5":
        print("\nAdd Member")

        member = Member(
            input("Member ID: "),
            input("Name: "),
            input("Email: "),
            input("Phone: ")
        )

        member_service.add_member(member)

        print("\nMember added successfully.")

    elif choice == "6":
        members = member_service.get_all_members()

        if not members:
            print("\nNo members available.")
        else:
            print("\n========== Members ==========")

            for member in members:
                print(member)

    elif choice == "7":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("\nInvalid choice.")