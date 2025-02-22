balance=1000
def check_balance(balance):
    return f"Your balance is: {balance} pounds."

def deposit(balance):
    add = float(input("Enter deposit amount: "))
    if add > 0:
        balance += add
        return f"Deposit amount:{balance}"
    else:
        return "Invalid deposit amount."

def withdraw(balance):
    withdraw_amount = float(input("Enter withdrawal amount: "))
    if withdraw_amount > balance:
        return "Insufficient funds!"
    elif withdraw_amount > 0:
        balance -= withdraw_amount
        print("f your balance is {balance}")
        return balance
    else:
        return "invalid withdrawal amount"
balance = 1000
while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(check_balance(balance))
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("Thank you for using Simple Bank System!")
            break
        else:
            print("Invalid choice! Please try again.")