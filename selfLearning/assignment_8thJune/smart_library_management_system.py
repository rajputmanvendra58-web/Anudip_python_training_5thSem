# Smart Library Management System
"""
Problem Statement 
Create a digital library management system. 
Example Structure 
library = {     "B101": {         
"title": "Python Basics",         
"author": "ABC",         
"copies": 5     } } 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase. 
"""
#===============================================================================
# Smart Library Management System Implementation
#===============================================================================
# dictionary to store book information
library = {}

#=================================================================================
# input details of 30 books
#=================================================================================
print("Enter details of 30 books:")
for i in range(30):
    print(f"\nBook {i+1}:")
    #---------------------------------------------------------------------------------
    #book ID validation
    #example: B101, B102, ..., B130
    #---------------------------------------------------------------------------------
    while True:
        book_id = input("Enter Book ID (e.g., B101): ").upper()
        if book_id in library:
            print("Book ID already exists. Please enter a unique ID.")
        elif book_id.startswith("B") and book_id[1:].isdigit() and len(book_id) == 4:
            break
        else:
            print("Invalid Book ID format. Please enter in the format B101, B102, etc.")

        #---------------------------------------------------------------------------------
        # book title validation
        #---------------------------------------------------------------------------------
        # book title should not be empty
        # ---------------------------------------------------------------------------------
    while True:
        title = input("Enter Book Title: ").strip()
        if title:
            break
        else:
            print("Book title cannot be empty. Please enter a valid title.")

        #---------------------------------------------------------------------------------
        # book author validation
        # ---------------------------------------------------------------------------------
        # book author should not be empty
        # ---------------------------------------------------------------------------------
    while True:
        author = input("Enter Book Author: ").strip()
        if author:
            break
        else:
            print("Book author cannot be empty. Please enter a valid author name.")

        #---------------------------------------------------------------------------------
        # book copies validation
        # ---------------------------------------------------------------------------------
        # book copies should be a positive integer
        # ---------------------------------------------------------------------------------    
    while True:
        try:
            copies = int(input("Enter Number of Copies: "))
            if copies >= 0:
                break
            else:
                print("Number of copies should be a positive integer. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of copies.")

            #---------------------------------------------------------------------------------
            #store book record in the library dictionary
            #---------------------------------------------------------------------------------
    library[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print("\n30 Books Recorded Successfully!")
#=================================================================================
# Menu-driven Program
#=================================================================================
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search a book by ID")
    print("4. Search by title")
    print("5. Update available copies")
    print("6. Issue a book")
    print("7. Return a book")
    print("8. Display books with fewer than 3 copies")
    print("9. Display books that are unavailable")
    print("10. Find the most available book")
    print("11. Generate a restocking report")
    print("12. Create a separate dictionary of books requiring immediate purchase")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")
    #=================================================================================
    # Add a book
    #=================================================================================
    if choice == '1':
        book_id = input("Enter Book ID (e.g., B101): ").upper()
        if book_id in library:
            print("Book ID already exists. Please enter a unique ID.")
        elif book_id.startswith("B") and book_id[1:].isdigit() and len(book_id) == 4:
            title = input("Enter Book Title: ").strip()
            author = input("Enter Book Author: ").strip()
            try:
                copies = int(input("Enter Number of Copies: "))
                if copies >= 0:
                    library[book_id] = {
                        "title": title,
                        "author": author,
                        "copies": copies
                    }
                    print("Book added successfully!")
                else:
                    print("Number of copies should be a positive integer.")
            except ValueError:
                print("Invalid input for number of copies. Please enter a valid integer.")
        else:
            print("Invalid Book ID format. Please enter in the format B101, B102, etc.")

        #=================================================================================
        # Remove a book
        #=================================================================================
    elif choice == '2':
        book_id = input("Enter Book ID to remove: ").upper()
        if book_id in library:
            del library[book_id]
            print("Book removed successfully!")
        else:
            print("Book ID not found. Please enter a valid ID.")

        #=================================================================================
        # Search a book by ID
        #=================================================================================
    elif choice == '3':
        book_id = input("Enter Book ID to search: ").upper()
        if book_id in library:
            book = library[book_id]
            print(f"Book ID: {book_id}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Copies Available: {book['copies']}")
        else:
            print("Book ID not found. Please enter a valid ID.")
        #=================================================================================
        # Search by title   
        #=================================================================================
    elif choice == '4':
        title = input("Enter Book Title to search: ").strip().lower()
        found_books = [book_id for book_id, book in library.items() if book['title'].lower() == title]
        if found_books:
            for book_id in found_books:
                book = library[book_id]
                print(f"Book ID: {book_id}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Copies Available: {book['copies']}")
        else:
            print("Book title not found. Please enter a valid title.")
        #=================================================================================
        # Update available copies
        #=================================================================================
    elif choice == '5':
        book_id = input("Enter Book ID to update copies: ").upper()
        if book_id in library:
            try:
                new_copies = int(input("Enter new number of copies: "))
                if new_copies >= 0:
                    library[book_id]['copies'] = new_copies
                    print("Book copies updated successfully!")
                else:
                    print("Number of copies should be a positive integer.")
            except ValueError:
                print("Invalid input for number of copies. Please enter a valid integer.")
        else:
            print("Book ID not found. Please enter a valid ID.")
        #=================================================================================
        # Issue a book
        #=================================================================================
    elif choice == '6':
        book_id = input("Enter Book ID to issue: ").upper()
        if book_id in library:
            if library[book_id]['copies'] > 0:
                library[book_id]['copies'] -= 1
                print("Book issued successfully!")
            else:
                print("Sorry, no copies of the book are available.")
        else:
            print("Book ID not found. Please enter a valid ID.")
        #=================================================================================
        # Return a book
        #=================================================================================
    elif choice == '7':
        book_id = input("Enter Book ID to return: ").upper()
        if book_id in library:
            library[book_id]['copies'] += 1
            print("Book returned successfully!")
        else:
            print("Book ID not found. Please enter a valid ID.")
        #=================================================================================
        # Display books with fewer than 3 copies    
        #=================================================================================
    elif choice == '8': 
        print("Books with fewer than 3 copies:")
        for book_id, book in library.items():
            if book['copies'] < 3:
                print(f"Book ID: {book_id}, Title: {book['title']}, Copies: {book['copies']}")
        #=================================================================================
        # Display books that are unavailable
        #=================================================================================
    elif choice == '9':
        print("Books that are unavailable:")
        for book_id, book in library.items():
            if book['copies'] == 0:
                print(f"Book ID: {book_id}, Title: {book['title']}")
            # ======================================================
    # Find Most Available Book
    # ======================================================

    elif choice == "10":

        most_available = None

        for bid in library:

            if most_available is None:

                most_available = bid

            elif library[bid]["copies"] > \
                 library[most_available]["copies"]:

                most_available = bid

        print("\nMost Available Book")

        print("Book ID :", most_available)
        print("Title   :",
              library[most_available]["title"])
        print("Author  :",
              library[most_available]["author"])
        print("Copies  :",
              library[most_available]["copies"])

    # ======================================================
    # Generate Restocking Report
    # Books Having Less Than 3 Copies
    # ======================================================

    elif choice == "11":

        print("\nRestocking Report")

        found = False

        for bid, details in library.items():

            if details["copies"] < 3:

                print(
                    bid,
                    details["title"],
                    "Copies =",
                    details["copies"]
                )

                found = True

        if found == False:

            print("No Book Requires Restocking.")

    # ======================================================
    # Create Immediate Purchase Dictionary
    # Books Having Zero Copies
    # ======================================================

    elif choice == "12":

        purchase_books = {}

        for bid, details in library.items():

            if details["copies"] == 0:

                purchase_books[bid] = details

        print("\nBooks Requiring Immediate Purchase")

        if len(purchase_books) == 0:

            print("No Books Require Immediate Purchase.")

        else:

            for bid, details in purchase_books.items():

                print(
                    bid,
                    details["title"],
                    "Copies =",
                    details["copies"]
                )

    # ======================================================
    # Exit Program
    # ======================================================

    elif choice == "13":

        print("\nProgram Terminated Successfully.")
        break

    # ======================================================
    # Invalid Choice Handling
    # ======================================================

    else:

        print("Invalid Choice. Please Enter 1 to 13.")
