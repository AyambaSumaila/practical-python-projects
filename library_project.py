import sys

class Library:
    def __init__(self, list, name):
        self.bookList=list
        self.name=name
        self.lenDict={}
    def displayBooks(self):
        print(f"\t\t\t{self.name}, we have the following books in our library")
        sno=1
        for book in self.bookList:
            print(f"\t\t\t{sno} {book}")
            sno +=1
            
    def lendBook(self, book, name):
        if book in self.bookList:
            if book not in self.lenDict:
                self.lenDict.update({book: name})
                print("\t\t\tLender-Book database has been updated. You can take a book now")
                
            else:
                 print(f"\t\t\tBook is already being used by {self.lenDict[book]}")
                 
                 
                 
        else:
              print(f"\t\t\tThis book is not related to our database")
    def addBook(self, book):
        self.bookList.append(book)
        print("\t\t\tBook has been added to the book list")
        
    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lenDict.keys():
                self.lenDict.pop(book)
                print("\t\t\tOk Thank you, Book is recived.")
            else:
                 print(f"\t\t\tThis book {book} is not in use.")
                
        else:
             print(f"\t\t\tThis book is not related to our database")
        


BenLibrary =  Library(['Python','Java','Data Science','Web Scraping','Data Mining'] , "Sumaila's")
while(True):
        print(f"\t\t\tWelcome to the {BenLibrary.name} library. Enter your choice to continue")
        print("\t\t\t1 Display Books")
        print("\t\t\t2 Lend a Book")
        print("\t\t\t3 Add a Book")
        print("\t\t\t4 Return a Book")
        print("\t\t\t5 Quit ")
        user_choice = input()
        
        if user_choice == 5:
            print('You have quitted the program')
            
            break
        elif user_choice not in ['1','2','3','4']:
            print("\t\t\tPlease enter a valid option")
            continue
        else:
              user_choice = int(user_choice)
        
        if user_choice == 1:
            BenLibrary.displayBooks()
            
        elif user_choice == 2:
            book = input("\t\t\tEntet the name of the book you want to lend:")
            user_name = input("\t\t\tEnter your name:")
            BenLibrary.lendBook(book,user_name)
        
        elif user_choice == 3:
            book = input("\t\t\tEnter the name of the book you want to add:")
            BenLibrary.addBook(book)
        
        elif user_choice == 4:
            book = input("\t\t\tEntet the name of the book you want to return:")
            BenLibrary.returnBook(book)
            
       
        else:
            print("\t\t\tNot a valid option")
            
            
        print("Press q to quit and c to continue")
        
        user_choice2 = ""
        
        while(user_choice2 != "c" and user_choice2 !="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
                
            elif user_choice2 == "c":
                continue
            
            