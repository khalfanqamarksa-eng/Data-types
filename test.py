class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"You have borrowed,  {self.title} by {self.author}.")
        else:
            print(f"No, {self.title} by {self.author} is already borrowed.")
    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"You have returned, {self.title} by {self.author}")
        else:
            print(f"{self.title} by {self.author} was not borrowed.")
book1 = Library("The Tale of the Cat" , "Jimmy Franks")
book2 = Library("The Tale of the Dog" , "Jimmy Franks")
book3 = Library("The Tale of the Bat" , "Jimmy Franks")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()

        
        
    