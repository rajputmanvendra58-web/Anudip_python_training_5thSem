    #Program for ATM Transaction History
    # Problem Statement 
    # A customer's transactions are stored as: 
    # transactions = [5000, -2000, 3000, -1000, -500, 7000]
    # Positive values represent deposits and negative values represent withdrawals.
    # Write a program to:
    # 1. Calculate the current balance.
    # 2. Count total deposits and withdrawals. 
    # 3 Find the largest deposit and largest withdrawal. 
    # 4.Create separate lists for deposits and withdrawals. 
    # List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Current balance starts from 0
balance = 0

# Lists to store deposits and withdrawals
deposits = []
withdrawals = []

# Traverse each transaction
for amount in transactions:
    balance += amount  # Add transaction to balance

    if amount > 0:
        deposits.append(amount)      # Store deposit
    else:
        withdrawals.append(amount)   # Store withdrawal

# Find largest deposit manually
largest_deposit = deposits[0]
for amount in deposits:
    if amount > largest_deposit:
        largest_deposit = amount

# Find largest withdrawal manually
largest_withdrawal = withdrawals[0]
for amount in withdrawals:
    if amount < largest_withdrawal:
        largest_withdrawal = amount

# Display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)