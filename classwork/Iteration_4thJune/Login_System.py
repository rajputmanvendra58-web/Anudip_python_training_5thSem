#Program to enter the correct password
password = input("Enter your password here")
while len(password) != 8:
    exit("Kindly Enter 8-Digit of Password")
while password != "admin123":
    password=input("Invalid Password")
print("Login Successfull")
