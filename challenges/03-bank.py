# print("Welcome to Chase bank.")
# print("Have a nice day!")

# ### Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance,
# withdraw or deposit. Write three methods to perform these calculations and
# output the result to the user.

# Gather user input using the `input` function. Note that input always returns
# user input as a string. You have to manually convert it to an int or a float
# to make it behave like number. Also, end the input prompt with a \n newline
# character if you want the user to type in on the next line.

# ```
# age = input("How old are you?\n")
# age = int(age)
# ```

# Here is a sample output:

# ```
# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!
# ```

current_balance = 4000

def deposit ():
    amount = input('How much would you like to deposit? ')
    new_balance = current_balance + int(amount)
    return print(f'Your current balance is {new_balance}')

def withdraw ():
    amount = input('How much would you like to withdraw? ')
    new_balance = current_balance - int(amount)
    return print(f'Your current balance is {new_balance}')

def check_balance ():
    return print(f'Your current balance is {current_balance}')

def option_question ():
    option = input('What would you like to do today? (deposit, withdraw, check_balance) ')
    if option == 'deposit':
        deposit()
    elif option == 'withdraw':
        withdraw()
    elif option == 'check_balance':
        check_balance()
    anything_else = input('Would you like to do anything else today? (yes, no) ')
    if anything_else == 'yes':
        option_question()
    elif anything_else == 'no':
        print('Thank you!')

def welcome ():
    print('Welcome to Rex bank')
    option_question()


welcome()
