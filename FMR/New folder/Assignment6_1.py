class BookStore:
    NoOfBooks = 0

    def __init__(self,bname,bauth):
        self.Name = bname
        self.Author = bauth
        BookStore.NoOfBooks +=1

    def Display(self):
        print(self.Name,"by ",end="")
        print(self.Author," "," ",end="")
        print("No of books",self.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()
    obj2 = BookStore("C Programming","Dennish Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()