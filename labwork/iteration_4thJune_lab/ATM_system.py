# ATM Simulation System
# Initial balance
balance = 10000

# Infinite loop to display menu repeatedly
while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Accept user's choice
    choice = int(input("Enter your choice: "))

    # Check balance
    if choice == 1:
        print("Current Balance = ₹", balance)

    # Deposit money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("Amount Deposited Successfully.")
        print("Updated Balance = ₹", balance)

    # Withdraw money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))

        # Check if sufficient balance is available
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful.")
            print("Remaining Balance = ₹", balance)
        else:
            print("Insufficient Balance!")

    # Exit from ATM
    elif choice == 4:
        print("Thank You for Using ATM.")
        break

    # Invalid choice
    else:
        print("Invalid Choice! Please try again.")