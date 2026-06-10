# Problem Statement 2: File Backup Utility 
"""
An organization wants to create backups of important text files to prevent accidental data loss. 
You have been asked to develop a utility that creates an exact copy of an existing file. 
Requirements 
Write a Python program that reads the entire contents of a source file and copies them into another destination file. 
The program should: 
1. Accept the names of the source file and destination file from the user.  
2. Read the complete contents of the source file.  
3. Write the contents into the destination file.  
4. Display a success message after the copying process is completed.
"""
#----------------------------------to make a copy of a file------------------------
# Input file names
# source_file = input("Enter source file name: ")
# destination_file = input("Enter destination file name: ")

# Open source file in read mode:
f1 = open(r"C:\Users\rajpu\OneDrive\Desktop\file_handling.txt", "r")
#----------------------------------------------------------------------------------
# Read all content:
content = f1.read()
#----------------------------------------------------------------------------------
# Close source file:
f1.close()
#----------------------------------------------------------------------------------
# Open destination file in write mode:
f2 = open(r"C:\Users\rajpu\OneDrive\Desktop\copy_file_handling.txt", "w")
#----------------------------------------------------------------------------------
# Write content to destination file:
f2.write(content)
#----------------------------------------------------------------------------------
# Close destination file:
f2.close()
#----------------------------------------------------------------------------------
# Print the code execution status:
print("File copied successfully!")
#----------------------------------------------------------------------------------