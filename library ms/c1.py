from typing import List
import exc
from pathlib import Path
b=[]
class Book:
    def __init__(self,name,isb,auth):
        self.name=name
        self.isbn=isb
        self.author=auth
        self.reserved=False
        self.available=True
            
    def borrow_book(self):
        if(self.available==False):
            print("Book is not available")
            return
        else:
            if(self.reserved==True):
                print("Book is reserved")
                return
            else:
                print("Book borrowed")
                self.available=False
                return

            
        
    def return_book(self):
        self.available=True
        print("Book returned")
            

    def reserve_book(self):
        self.reserved=True
        print("Book is reserved")
        
        

class Shelf:
    b:List[Book]
    def __init__(self):
        pass
    def show_catalog(self):
        for bk in self.b:
            if(bk.available==True):
                print("Book Name : {} Book ISBN : {} Book Author : {}\n".format(bk.name,bk.isbn,bk.author))
            
            
    def add_book(self,bk:Book):
        self.b.append(bk)
        print("Book added")
        
        
    def remove_book(self,k):
        for bk in b:
            if(self.b==k):
                self.b.remove(bk)
                print("Book removed")
                return
        print("Book not present")

    def get_books_count(self):
        l=0
        for bk in self.b:
            if(bk.available==True):
                l=l+1
        print("Number of available books = ",l)

    def populate_books(self,filename):
        t=Path('',filename)
        if( t.exists==False):
            print("File ",filename,"not found")
            return
        else:
            bkl=exc.populate(filename)
            for b1 in bkl:
                b.append(b1)
            print("Books added")
            return

class User:
    def __init__(self):
        self.us="User"
    def check(self,pwd):
        if(pwd=='librarian123'):
            self.us="Librarian"
            print("Librarian logged in")
            return
        else:
            print("Normal User Login")
        
def main():
    user=User()
    shelf=Shelf()
    shelf.populate_books("data.xlsx")
    while True:

        print("1: Login \n2: Show catalog of books \n3: Add book in catalog \n4:Remove book in catalog \n 5:Borrow book\n 6:Return book\n7:Reserve book\n 8:Number of books\n 9:Import catalog ")
        i=int(input("Enter index for function"))
        if(i==1):
            if user.us=="Librarian":
                print("Already logged in")
                continue
            id=input("Enter ID\n")
            pw=input("Enter pwd\n")

        elif(i==2):
            if user.us=="Librarian":
                shelf.show_catalog()
            else:
                print("You do not have Librarian access")
            continue
        elif(i==3):
            if user.us=="Librarian":
                nm=input("Enter Name of Book")
                isb=int(input("Enter ISBN "))
                au=input("Enter author name")
                k=Book(nm,isb,au)
                shelf.add_book(k)
            else:
                print("You do not have librarian access")
            continue
        elif(i==4):
            if user.us=="Librarian":
                isb=int(input("Enter ISBN "))
                shelf.remove_book(isb)
            else:
                print("You do not have librarian access")
            continue
        elif(i==5):
            isb=int(input("Enter ISBN "))
            for bk in shelf.b:
                if(bk.isbn==isb):
                    bk.borrow_book()
                    break
            continue
        elif(i==6):
            isb=int(input("Enter ISBN "))
            for bk in shelf.b:
                if(bk.isbn==isb):
                    bk.return_book()
                    break
            continue
        elif(i==7):
            isb=int(input("Enter ISBN "))
            for bk in shelf.b:
                if(bk.isbn==isb):
                    bk.reserve_book()
                    break
            continue
        elif(i==8):
            if user.us=="Librarian":
                print("Number of books",shelf.get_books_count())
            else:
                print("You do not have librarian access")
            continue
        elif(i==9):
            if user.us=="Librarian":
                fl=input("Enter filename")
                shelf.populate_books(fl)

            else:
                print("You do not have librarian access")

            continue
        elif(i==10):
            print("Program ends")
            break

main()



