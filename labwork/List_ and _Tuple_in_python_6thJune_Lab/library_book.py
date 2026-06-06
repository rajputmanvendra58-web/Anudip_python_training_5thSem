# Program for Library Book Search
""" 
 Problem Statement 
 Books available in a library: 
 books = [     
 ("Python Basics", 5),     
 ("Data Science", 0),     
 ("Java Programming", 3),     
 ("Machine Learning", 0) ]
 Write a program to: 
 • Display unavailable books.  
 • Find all books with more than 2 copies.  
 • Count available books.  
 • Stop searching once a requested book is found.
 """

 # Task 1: Store book names and available copies

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Task 2: Display unavailable books

print("---------------Unavailable Books:--------------")
for book in books:
    if book[1] == 0:
        print(book[0])

# Task 3: Find books having more than 2 copies

print("-------------------------------\nBooks with more than 2 copies:-------------------------------------")
for book in books:
    if book[1] > 2:
        print(book[0])

# Task 4: Count available books

available_count = 0

for book in books:
    if book[1] > 0:
        available_count += 1

print("----------------------------------\nNumber of available books:-----------------------------------", available_count)

# Task 5: Stop searching once requested book is found

search_book = input("\nEnter book name to search: ")

for book in books:
    if book[0].lower() == search_book.lower():
        print("Book Found!")
        print("Copies Available:", book[1])
        break
else:
    print("--------------------------------------------Book Not Found!--------------------------------------")