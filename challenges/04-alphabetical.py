# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# ### Challenge 4 - Sort a String

# Create a function that takes a string and returns the string with the letters in 
# alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation 
# symbols will not be included in the string.

# ```
# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
# ```

def alphabetize_string (string):
    new_list = []
    for i in range(len(string)):
        new_list.insert(0, string[i])
    new_list.sort()
    new_string = ("").join(new_list)
    return print(f'Alphabetized: {new_string}')

a_string = input('Give me a string to alphabetize: ')

alphabetize_string(a_string)