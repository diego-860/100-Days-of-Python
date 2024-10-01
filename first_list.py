# states_of_america = ["Connecticut", "Pennsylvania", "Virginia", "Florida"]

import random

states_of_america = ["Delaware", "Pennsylvania",
                     "New Jersey", "Georgia", "Connecticut"]

# Fetching the 5th item in the list because we count from 0
print(states_of_america[4])
# Fetching the last item in the list because we're counting backwards
# When going backwards - we start from 1 because -0 does not exist
print(states_of_america[-1])
# Assigning a new value to the index
states_of_america[1] = "Pencilvania"
# Add a new item to the list
states_of_america.append("Massachusettes")

print(states_of_america)

# Extend a list by adding a new list to the existing list
states_of_america.extend(
    ["Maryland", "South Carolina", "New Hampshire", "Virginia"])

print(states_of_america)

print(states_of_america[random.randint(0, 4)])
