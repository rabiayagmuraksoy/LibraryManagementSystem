class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.file = open(self.filename, 'a+')
        self.file.seek(0)
        if not self.file.read(1):
            self.file.write("Book Title,Author,Release Date,Number of Pages\n")
            self.add_initial_books()

    def __del__(self):
        self.file.close()

    def add_initial_books(self):
        initial_books = [
            "Harry Potter and the Sorcerer's Stone,J.K. Rowling,1997,320\n",
            "The Hobbit,J.R.R. Tolkien,1937,310\n",
            "A Game of Thrones,George R.R. Martin,1996,694\n",
            "The Name of the Wind,Patrick Rothfuss,2007,662\n",
            "Mistborn: The Final Empire,Brandon Sanderson,2006,541\n",
            "The Lies of Locke Lamora,Scott Lynch,2006,499\n",
            "The Way of Kings,Brandon Sanderson,2010,1007\n",
            "The Priory of the Orange Tree,Samantha Shannon,2019,827\n",
            "The Eye of the World,Robert Jordan,1990,814\n",
            "The Poppy War,R.F. Kuang,2018,530\n",
            "Shadow and Bone,Leigh Bardugo,2012,358\n",
            "The Hunger Games,Suzanne Collins,2008,374\n",
            "Twilight,Stephenie Meyer,2005,498\n",
            "The Maze Runner,James Dashner,2009,375\n",
            "The Fellowship of the Ring,J.R.R. Tolkien,1954,479\n",
            "The Lion, the Witch and the Wardrobe,C.S. Lewis,1950,206\n",
            "The Alchemist,Paulo Coelho,1988,197\n",
            "Eragon,Christopher Paolini,2002,509\n",
            "The Chronicles of Narnia,C.S. Lewis,1950,767\n"
        ]

        for book_info in initial_books:
            self.file.write(book_info)

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        if len(lines) > 1:
            header, *book_lines = lines
            for line in book_lines:
                book_info = line.split(',')
                print(f"Book: {book_info[0]}, Author: {book_info[1]}")
        else:
            print("No books available.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        print(f"Book '{title_to_remove}' removed successfully.")


if __name__ == "__main__":
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")

        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            print("Exiting the Library Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")
