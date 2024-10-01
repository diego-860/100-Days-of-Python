""" Module utilizing the random module to create a coin flipper"""

import random

# Return a random integer N such that a <= N <= b
# random_integer = random.randint(1, 10)
# print(random_integer)


# Return the next random floating-point number in the range 0.0 <= X < 1.0
# Muliply by 10 and round to whole number
# random_number_0_to_1 = round(random.random() * 10)

# Return a random floating-point number N such that a <= N <= b
# random_float = random.uniform(1, 10)
# print(random_float)

# Random between a range of 0-1
coin = random.randint(0, 1)

if coin == 1:
    print("Tails")
else:
    print("Heads")
