# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# ### Challenge 1 - Calculator

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

operator = input('What calculation would you like to do? (add, sub, mult, div) ')
num1 = input('What is number 1? ')
num2 = input('What is number 2? ')

def calculate(operator, num1, num2):
    if operator == 'add':
        return print(f'Your result is {int(num1)+int(num2)}')
    elif operator == 'sub':
        return print(f'Your result is {int(num1)-int(num2)}')
    elif operator == 'mult':
        return print(f'Your result is {int(num1)*int(num2)}')
    elif operator == 'div':
        return print(f'Your result is {int(num1)/int(num2)}')

calculate(operator, num1, num2)