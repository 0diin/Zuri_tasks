class Budget:
    '''This is a budget app'''

    def __init__(self, name, size):
        self.budget_name = name
        self.budget_size = size

    def deposit(self):
        print(f'How much would you like to add to the budget of {self.budget_size}? \n')
        dep_funds = int(input())
        print(f'Do you want to approve the deposit of {dep_funds}? \n')
        print('Press 1 to approve and 2 to cancel')
        auth = int(input())
        while not auth:
            if auth == 1:
                auth == True
                print('Deposit approved!')
            if auth == 2:
                auth == True
                print('Cancelled!')
            else:
                print('Invalid Selection')
                break

    def withdraw(self):
        # Withdraw funds from any of the budget categories
        print('How much would you like to withdraw? \n')
        amt_withdraw = int(input())
        print('What category do you want to withdraw from? \n')
        print('1. Food 2. Clothing 3. Data 4. Entertainment 5. Healthcare \n')
        cat_withdraw = int(input())

        if amt_withdraw <= budget_1.budget_size:
            print('Successful')
            self.homepage(self)
        elif amt_withdraw <= budget_2.budget_size:
            print('Successful')
            self.homepage(self)
        elif amt_withdraw <= budget_3.budget_size:
            print('Successful')
            self.homepage(self)
        elif amt_withdraw <= budget_4.budget_size:
            print('Successful')
            self.homepage(self)
        elif amt_withdraw <= budget_5.budget_size:
            print('Successful')
            self.homepage(self)
        else:
            print('Insufficient funds in target category')
            self.homepage(self)


    def balance(self):
        # Return balance for any budget category when called in respect to that category
        print('What budget category would you want to see balance left \n')
        print('1. Food 2. Clothing 3. Data 4. Entertainment 5. Healthcare \n')
        bal_category = int(input())
        if bal_category == 1:
            return budget_1.budget_size
        elif bal_category == 2:
            return budget_2.budget_size
        elif bal_category == 3:
            return budget_3.budget_size
        elif bal_category == 4:
            return budget_4.budget_size
        elif bal_category == 5:
            return budget_5.budget_size
        else:
            pass

    def transfer(self):
        # Transfer funds between different categories and return balances
        print('How much would you like to transfer? \n')
        amt_transfer = int(input())
        print('What budget category would you like to transfer to?')
        print('1. Food 2. Clothing 3. Data 4. Entertainment 5. Healthcare \n')
        cat_transfer = int(input())
        if cat_transfer == 1:
            amt_transfer + budget_1.budget_size
            return
        elif cat_transfer == 2:
            amt_transfer + budget_2.budget_size
            return
        elif cat_transfer == 3:
            amt_transfer + budget_3.budget_size
            return
        elif cat_transfer == 4:
            amt_transfer + budget_4.budget_size
            return
        elif cat_transfer == 5:
            amt_transfer + budget_5.budget_size
            return
        else:
            print('Invalid selection!')
            self.transfer(self)

    def homepage(self):
        # Acts aas the reception from where different methods can be called based on inputs
        print('Welcome, what would you like to do?')
        print('Press 1. To Withdraw \n Press 2. To deposit \n Press 3. For Budget balance \n Press 4. To Transfer \n')
        home_options = int(input())
        if home_options == 1:
            self.withdraw(self)
        elif home_options == 2:
            self.deposit(self)
        elif home_options == 3:
            self.balance(self)
        elif home_options == 4:
            self.transfer(self)
        else:
            print('Invalid selection, Try again')


budget_1 = Budget('Food', 20000)
budget_2 = Budget('Clothing', 10000)
budget_3 = Budget('Data', 8000)
budget_4 = Budget('Entertainment', 6000)
budget_5 = Budget('Healthcare', 5000)

################### BUDGET APP ##############################


