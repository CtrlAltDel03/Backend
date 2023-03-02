import exc
j=11
b=[]
id=0
count=0
class Book:
    def __init__(self,name,isb,auth):
        self.name=name
        self.isbn=isb
        self.author=auth
        b.append(self)
            
    i=0
    def borrow_book(self,d):
        t=0
        k=0
        if(d==id):
            if(j<count and self==b[j]):
                b.pop(j)
                print("Reserved Book Borrowed")
            else:
                for k in count:
                    if(self==b[k]):
                        b.pop(k)
                        print("Book borrowed")
                        t=k
                        break
                    k=k+1
                if(t==0):
                    print("Book out of stock")
        else:                
            if(self==b[j]):
                print("Book is reserved")
            else:
                for k in count:
                    if(self==b[k]):
                        b.pop(k)
                        count=count-1
                        print("Book borrowed")
                        t=k
                        break
                    k+=1
                if(t==0):
                    print("Book out of stock")
            
        
    def return_book(self):
        b.append(self)
        print("Book returned")
            

    def reserve_book(self,d):
        i=0
        for i in count:
            if(self==b[i]):
                j=i
                id=d
                break
            i=i+1
        

class Shelf:
    def _init(self):
        pass
    def show_catalog(self):
        l=self.len()
        i=0
        for i in l:
            print("Book Name : {} Book ISBN : {} Book Author : {}\n".format(self[i].name,self[i].isbn,self[i].author))
            i=i+1
            
    def add_book(self,b):
        self.append(b)
        print("Book added")
        
        
    def remove_book(self,b):
        self.pop(b)
        
        print("Book removed")

    def get_books_count(self):
        l=0
        for i in self:
            l+=1
        print("Number of books = ",l)

    def populate_books(self):
        self=exc.populate()
        print("Books added")


            

