import operator
from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, author, title, date):
        self.author = author
        self.title = title
        self.date = date

    def __lt__(self, other):
        return self.author < other.author

    def __eq__(self, other):
        return self.author == other.author


def add_book(books):
    author = input("\t\t\tEnter the author's name: ")
    title = input("\t\t\tEnter the book's title: ")
    date = input("\t\t\tEnter the publication date (dd/mm/yy or dd-mm-yy): ")

    if not is_valid_date(date):
        print(
            "\t\t\tInvalid date. Please enter the date in the format dd/mm/yy or dd-mm-yy.")
        return

    if title.isdigit():
        print("Invalid title. Title cannot be numeric.")
        return

    book = Book(author, title, date)
    books.append(book)
    print("\t\t\tBook added successfully!")


def delete_book(books):
    author = input("\t\t\tEnter the author's name: ")
    title = input("\t\t\tEnter the book's title: ")
    date = input("\t\t\tEnter the publication date (dd/mm/yy or dd-mm-yy): ")

    matching_books = []
    for book in books:
        if book.author == author and book.title == title and book.date == date:
            matching_books.append(book)

    if len(matching_books) == 0:
        print("\t\t\tNo matching books found.")
        return

    print(f"\t\t\tFound {len(matching_books)} matching book(s):")
    for i, book in enumerate(matching_books, start=1):
        print(
            f"\t\t\t{i}. Author: {book.author}\tTitle: {book.title}\tDate: {book.date}")

    choice = input("\t\t\tEnter the number of the book to delete: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(matching_books):
            book = matching_books[choice - 1]
            books.remove(book)
            print("\t\t\tBook deleted successfully!")
        else:
            print("\t\t\tInvalid choice.")
    except ValueError:
        print("\t\t\tInvalid choice.")


def is_valid_date(date):
    # Check if the date is in the valid format (dd/mm/yy or dd-mm-yy)
    date_parts = date.split("/")
    if len(date_parts) != 3:
        date_parts = date.split("-")
        if len(date_parts) != 3:
            return False

    day, month, year = date_parts
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    # Validate the day, month, and year values
    if not (1 <= day <= 31):
        return False

    if not (1 <= month <= 12):
        return False

    if not (0 <= year <= 99):
        return False

    return True


def print_books(books):
    # Sort the books by author name
    sorted_books = sorted(books, key=operator.attrgetter("author"))
    for book in sorted_books:
        # Print the book details
        print(
            f"\t\t\tAuthor: {book.author}\tTitle: {book.title}\tDate: {book.date}")


def main():
    books = []
    while True:
        print()
        print()
        print()
        print('\t\t\tHELLO THERE WELCOME TO ABC BOOK STORE DATABASE')

        print("\n\t\t\t************ Main Menu ***************")
        print()
        print("\t\t\t1. Add a book")
        print()
        print("\t\t\t2. Print alphabetical list of books")
        print()
        print("\t\t\t3. Delete a book")
        print()
        print("\t\t\t4. Quit")
        print()
        choice = input("\t\t\tEnter your choice (1-4): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            if len(books) == 0:
                print("\t\t\tNo books in the database.")
            else:
                print_books(books)
        elif choice == "3":
            if len(books) == 0:
                print("\t\t\tNo books in the database.")
            else:
                delete_book(books)
        elif choice == "4":
            print('\t\t\tThank for using the Application')
            print("\t\t\tExiting the program...")
            break
        else:
            print("\t\t\tInvalid choice. Please try again.")


if __name__ == '__main__':
    main()
