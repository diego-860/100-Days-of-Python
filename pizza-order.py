# Welcome the customer
print("Welcome to Diego's Pizza Palace")
# Ask customer for size of pizza
size = input("What size pizza would you like? S, M, or L: ")
# Ask customer if they'd like pepperoni on their pizza
pepperoni = input("Would you like pepperoni on your pizza? Y or N: ")
# Ask customer if they'd like extra cheese on their pizza
extra_cheese = input("Would you like extra cheese? Y or N: ")
# Create bill variable
bill = 0
# If Statement regarding if customer orders a "L" pizza
if size == "L":
    # Bill set for a "L" pizza
    bill = 25
    # If the customer input "Y" for the pepperoni question
    if pepperoni == "Y":
        # Increment bill +3 (only for "L" and "M" sizes)
        bill += 3
    # If the customer input "Y" for the extra cheese question
    if extra_cheese == "Y":
        # Increment bill +1
        bill += 1
# Else If Statement regarding if customer orders a "M" pizza - only executed if the above "If" is not executed
elif size == "M":
    # Bill set for a "M" pizza
    bill = 20
    # If the customer input "Y" for the pepperoni question
    if pepperoni == "Y":
        # Increment bill +3 (only for "L" and "M" sizes)
        bill += 3
    # If the customer input "Y" for the extra cheese question
    if extra_cheese == "Y":
        bill += 1
# Else If Statement regarding if customer orders a "S" pizza - only executed if the above "If" is not executed
elif size == "S":
    # Bill set for a "S" pizza
    bill = 15
    # If the customer input "Y" for the pepperoni question
    if pepperoni == "Y":
        # Increment bill +2 (only for "S" size)
        bill += 2
    # If the customer input "Y" for the extra cheese question
    if extra_cheese == "Y":
        # Increment bill +1
        bill += 1
# Print the customers total bill
print(f"Your total bill is ${bill}")


# to-do: work out how much they need to pay based on their size choice.

# to-do: work out how much to add to their bill baed on their pepperoni choice.

# to-do: work out their final amount based on whether if they want extra cheese.

# Small pizza = $15
# Medium pizza = $20
# Large pizza = $25
# add pepperoni for small = $2
# add pepperoni for medium or large = $3
# add extra cheese for any pizza = $1


bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You type the wrong inputs.")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
