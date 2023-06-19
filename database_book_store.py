# Import the necessary libraries
from __future__ import print_function
import sys

# Define the Book class
class Book:
  def __init__(self, author, title, date):
    self.author = author
    self.title = title
    self.date = date

  def __lt__(self, other):
    return self.author < other.author

# Create a vector to store the books
books = []

# Create a main menu
while True:
  print("Select from the following choices:")
  print("1. Add new book.")
  print("2. Print listing sorted by author.")
  print("3. Quit.")

  choice = input()

  if choice == "1":
    # Get the book's author, title, and date
    author = input("Enter author: ")
    title = input("Enter title: ")
    date = input("Enter date: ")

    # Add the book to the vector
    books.append(Book(author, title, date))
  elif choice == "2":
    # Sort the books by author
    books.sort()

    # Print the books
    for book in books:
      print(book.author, book.title, book.date)
  else:
    break

# Exit the program
sys.exit()
