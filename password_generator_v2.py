'''Password Generator module'''
import random

# Create lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome user
print("Welcome to the PyPassword Generator!")

# Prompt user for # of characters for each list
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Initialize password variable
password = ""

# Loop through each list using the amount of characters chosen via range
for char in range(0, nr_letters):
    # Add random choice of characters from list to password variable
    password += random.choice(letters)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

# Print password
print(password)

# Shuffle password
shuffled_password_list = list(password)
random.shuffle(shuffled_password_list)
shuffled_password = "".join(shuffled_password_list)
# Print shuffled password
print(f"Your password is: {shuffled_password}")
