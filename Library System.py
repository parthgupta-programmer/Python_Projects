#Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class
# Show how you can:
# 1. print all books, 
# 2. Add a book and get the number of books using different methods. 
# 3. Show that your program doesnt persist the books after the program is stopped!



# 📚 Functional Enhancements:
# 1.Add functionality for removing a book.
# 2.Support checking out and returning books.
# 3.Track which user borrowed which book.
# 4.Prevent a book from being checked out twice.
# 5.Allow searching for books by title or author.


class Library:
    def __init__(self, no_of_books, books):
        self.no_of_books=no_of_books
        self.books=books
    def print_all_books(self):
        print("All Books:\n")
        for i in range(len(self.books)):
            print(f"{i+1}.{(self.books).values[i]}")
        print("\n")
    def add_book(self,new_book_name):
        self.new_book_name=new_book_name
        (self.books).append(self.new_book_name)
        self.no_of_books+=1
    @property
    def nob(self):
        return self.no_of_books
    def remov(self,remove_name):
        a=0
        for i in range(len(self.books)):
            if(self.books[i]!=remove_name):
                a+=1
        if(a==len(self.books)):
            print("No book found with this name to remove.")
        else:
            (self.books).remove(remove_name)
    def search(self,t_name):
        for x,y in (self.books).items():
            if(x==t_name or y==t_name):
                print(f"Book Found.")
                print(f"NO of Books present:{self.no_of_books}")
    

    
    
l1=Library(10,{"Deep Work":"Cal Newport","The Alchemist":"Paulo Coelho","Rich Dad Poor Dad":"Robert Kiyosaki and Sharon Lechter","Gulliver's Travels":"Jonathan Swift","The Invisible Man":"H.G. Wells","The Bible":"Moses,David and Paul","The Diary of a Young Girl":
           "Anne Frank","Atomic Habits":"James Clear","Power of the Subconscious Mind":"Joseph Murphy","The Time Machine":"H.G. Wells"})

print("Before adding a book:")
l1.print_all_books()    
print("No. of Books:",l1.nob)

print("\n")


print("After adding a book:")
l1.add_book("Too Good Too be True")
l1.print_all_books()
print("No.of Books",l1.nob)

print("\n")

print("After removing a book")
l1.remov("Gulliver's Travels")
l1.print_all_books()

l1.search("James Clear")