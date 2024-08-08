#banking system

def menu():
    print("Welcome To StateBank Of Pakistan:")
    print("1. Deposit Money. \n2. WithDraw Your Money.\n3. Currency Exchange. \n4. Forex Trading. \n5. Exit")

def deposite_money():
    amount = float(input("Enter the amount to deposite: "))
    global balance
    balance += amount
    print(f"{amount} is deposited. Your new amount is here {balance}")

def withdraw_money():
    amount = float(input('Enter The Amount To Withdraw: '))
    global balance
    if amount > balance:
        print("Insuffient Amount. ")
    balance -=amount
    print(f"{amount} is withdrawed. Your Remaining amount is {balance}")

def currency_exchange():
    amount = float(input('Enter The amount to Exchange: '))
    exchange_rate = float(input("Enter The exchange Rate: "))
    exchanged_amount = amount*exchange_rate
    print(f'You have exchanged the {amount} with rate of {exchange_rate}, You get {exchanged_amount} ')

def forex_trade():
    amount = float(input("Enter THE amount for Forex Trading: "))
    profit_rate = float(input("Enter Thr PRofit Rate: "))
    profit = amount*profit_rate
    print(f"You have made a profit of {profit} from Forex Trading.")
balance = 0
while True:
    menu()
    user_choice= input("Whats Your Purpose: ")
    if user_choice == '1':
        deposite_money()
    elif user_choice== '2':
        withdraw_money()
    elif user_choice == '3':
        currency_exchange()
    elif user_choice == '4':
        forex_trade()
    elif user_choice == '5':
        print("Thank You So Much For Using State Bank Of Pakistan GoodBye!")
        break
    else:
        print("Please Enter The Correct Value: ")
