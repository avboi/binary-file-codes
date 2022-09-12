# QI. A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# 1. Write a user defined function CreateFileO to input data for a record and add to Book.dat .
# 2. Write a function CountRec(Author) in Python which accepts the Author name as parameter and count and return number of books by the given Author are stored in the binary file "Book.dat

import pickle

def CreateFile():
    bookdat = open("book.dat", 'ab+')
    bookno = int(input("Input book no: "))
    book_name = input("Type in book name: ")
    Author = input("Type in author: ")
    Price = int(input("Price of the book: "))
    booklist = [bookno, book_name, Author, Price]
    pickle.dump(booklist,bookdat)
    
    
def CountRec(Author):

    fobj=open("book.dat", "rb")
    num = 0
    while True:
        try:
            rec=pickle.load(fobj)
            if Author == rec[2]:
                num = num + 1

        except:
            fobj.close()
        return num

CreateFile()

Author = input("Enter author name to search:")
k = CountRec(Author)
print(k)
