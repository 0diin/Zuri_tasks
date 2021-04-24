import random


def initialize():
    valid_option_selected = False
    print('Welcome to Bank of Asgard')
    print('Do you have an account with us?')
    print('Press 1 for Yes 2. for No')
    option_selected = int(input())

    while option_selected is False:
        if valid_option_selected == 1:
            valid_option_selected = True
            print('Input login details \n')
            login()
        elif valid_option_selected == 2:
            valid_option_selected = True
            print('Register with us \n')
            register()
        else:
            print('Invalid option selected \n')
            initialize()


def generate_account_number():
    random.randrange(10000000000, 9999999999)
    return


# using registered details to login
def login():
    print('Please login with your correct details')
    print('What is your account number? \n')
    input_acc = int(input())
    if input_acc in user_details.keys():
        print('What is your password? \n')
        passkey = input()
        if passkey in user_details.values():
            print('Login successful')
            print('Welcome ' + str(user_details.values[0]))
            bank_operations()
        else:
            print('Incorrect password')
            login()
    else:
        print('Incorrect login password')
        login()


def register():
    print('Please input your First name \n')
    first_name = input()
    print('Please input your Last name \n')
    last_name = input()
    print('Please input your email address \n')
    email = input()
    print('Please input your desired password \n')
    password = input()



account_number = generate_account_number()
print('Your account has been created')
print('Your account number is: ' + str(account_number))
print('Please make sure to keep your details safe')
user_details = {account_number: ['first_name', 'last_name', 'email', 'password']}
balance = 400000000


def withdrawal():
    requestedFunds = int(input())
    if requestedFunds <= balance:
        print('Take your cash')
    else:
        print('Insufficient funds')


def deposit():
    print('How much would you like to deposit? \n')
    newAmountDeposited = int(input())
    new_balance = balance + newAmountDeposited
    print('Deposit Successful!')
    print('Your new balance is ' + str(new_balance) + 'NGN')


def complaint():
    print('What issue would you like to report? \n')
    issue = input()
    print(issue)
    print('Your issue has been taken note of')
    print('it will be resolved as soon as possible')
    print('Thank you for contacting Customer care, Do have a nice day')
    logout()


def logout():
    login()


def bank_operations():
    print('Welcome,' + str(user_details.values[0]) + ' you are logged in!')
    from datetime import datetime
    now = datetime.now()
    print('Today information is ' + str(now))
    option = int(input())
    print('Please select an option')
    print('1. Withdraw 2. Deposit 3. Complaint 4. Logout 5. Exit')
    if option == 1:
        print('How much would you like to withdraw? \n')
        withdrawal()
    elif option == 2:
        deposit()
    elif option == 3:
        complaint()
    elif option == 4:
        logout()
    elif option == 5:
        exit()
    else:
        print('Invalid option selected')
        bank_operations()


initialize()
