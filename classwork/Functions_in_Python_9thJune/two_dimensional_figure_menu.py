# Program for The operations of two-dimensional figures
"""
Problem Statement:
Create a program which provides a menu to the user to select a two-dimensional figure (rectangle, square, circle).
After selecting the figure user is again asked to provide the input of corresponding data for for the figure .
After input og corresponding data again provide a menu to the user to select the operation (area, perimeter) to be performed on the figure.
and as per the user selection perform the operation and display the result to the user.
This task is repeated again and again until the user selects the option to exit from that figure and back to previous menu to select another figure or exit from the program.
Also giving the user an option to perform another operation on the same figure without going back to the previous menu.
"""
# import the mensuration module
import mensuration
## Import the mensuration module
import mensuration

# Main loop for the application
while True:

    # Display figure menu
    print("\nSelect a two-dimensional figure:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # ------------------------- Rectangle -------------------------
    if choice == 1:

        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
            continue

        while True:

            print("\nSelect an operation:")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = mensuration.rectangle_area(length, width)
                print("The area of the rectangle is:", area)

            elif operation == 2:
                perimeter = mensuration.rectangle_perimeter(length, width)
                print("The perimeter of the rectangle is:", perimeter)

            elif operation == 3:
                break

            else:
                print("Invalid operation choice!")
                continue

            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # ------------------------- Square -------------------------
    elif choice == 2:

        side = float(input("Enter the side of the square: "))

        if side <= 0:
            print("Side must be a positive number.")
            continue

        while True:

            print("\nSelect an operation:")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")
            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = mensuration.square_area(side)
                print("The area of the square is:", area)

            elif operation == 2:
                perimeter = mensuration.square_perimeter(side)
                print("The perimeter of the square is:", perimeter)

            elif operation == 3:
                break

            else:
                print("Invalid operation choice!")
                continue

            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # ------------------------- Circle -------------------------
    elif choice == 3:

        radius = float(input("Enter the radius of the circle: "))

        if radius <= 0:
            print("Radius must be a positive number.")
            continue

        while True:

            print("\nSelect an operation:")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")
            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = mensuration.circle_area(radius)
                print("The area of the circle is:", area)

            elif operation == 2:
                perimeter = mensuration.circle_perimeter(radius)
                print("The perimeter of the circle is:", perimeter)

            elif operation == 3:
                break

            else:
                print("Invalid operation choice!")
                continue

            again = input(
                "Do you want to perform another operation on the same figure? (Y/N): "
            )

            if again.upper() != "Y":
                break

    # ------------------------- Exit -------------------------
    elif choice == 4:
        print("Thank you for using the application. Goodbye!")
        break

    # ------------------------- Invalid Figure Choice -------------------------
    else:
        print("Invalid figure choice! Please try again.")
        continue

    # Ask user whether to continue using the application
    continue_app = input(
        "\nDo you want to continue using the application? (Y/N): "
    )

    if continue_app.upper() != "Y":
        print("Thank you for using the application. Goodbye!")
        break