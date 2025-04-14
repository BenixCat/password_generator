# Importing the random module to generate random numbers
import random

# This is a password generator program that generates a random password based on user input for the number of letters, symbols, and numbers.
# The program uses the random module to select random characters from predefined lists of letters, symbols, and numbers.
# The user is prompted to input the desired number of letters, symbols, and numbers for the password.
# The program then generates a password by concatenating the selected characters and shuffling them to create a random order.
# Finally, the generated password is printed to the console.

# Providing the letters, symbols, and numbers to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Prompting the user for input on the number of letters, symbols, and numbers to include in the password
print("Welcome to the PyPassword Generator!")
# The user is asked how many letters, symbols, and numbers they want in their password.
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Generating a password based on the user's input
# Generating a empty password string
password = ""
# Selecting random letters, symbols, and numbers based on the user's input
for char in range(0, nr_letters):
    password += random.choice(letters)

for char1 in range(0, nr_symbols):
    password += random.choice(symbols)

for char2 in range(0, nr_numbers):
    password += random.choice(numbers)

# Shuffling the password to create a random order and printing it
# The password is shuffled to ensure that the order of characters is random.
print(''.join(random.sample(password,len(password))))
