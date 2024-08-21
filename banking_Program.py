
def show_balance(balance):
    print("******************************")
    print(f" Your balance is ${balance:.2f} ")
    print("******************************")

def deposit():
    print("******************************")
    amount = float(input("Enter the amount to deposit: "))
    print("******************************")
    if amount < 0 :
        print("Not a valid amount")
        return 0 
    else:
        return amount   

def withdraw(balance):
    print("******************************")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("******************************")
    if amount > balance:
        print("Insuficient Funds")
        return 0 
    elif amount < 0:
        print("Enter the valid amount")
        return 0 
    else:
        return amount

def main():    

    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("Welcome to the Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************************")

        choice = input("Enter your choice from 1 - 4: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("******************************")
            print("enter the valid choice")
            print("******************************")
    print("******************************")
    print("Thanks for choosing our bank")
    print("******************************")
if __name__ == '__main__':
    main()