'''Who will pay the bill'''

import random

# Create the list of patrons
patrons = ["Diego", "Samantha", "Amelia", "Lorelei"]

# Print list of patrons - but use the "random.randint" to select an index
print(patrons[random.randint(0, 3)])

# Use the "random.choice" function to select a random index for a sequence (list)
print(random.choice(patrons))

print(len(patrons))

num_of_patrons = len(patrons)

print(patrons[num_of_patrons - 1])


# This scenario is a banquet with 5 separate tables, 5 separate lists
# and will randomly select the table that wins the prize pays

table1 = ["Diego", "Samantha", "Amelia", "Lorelei"]
table2 = ["Edna", "Beba", "Troy", "Jayvon", "Jayden", "J'noah"]
table3 = ["Carolina", "Mike", "Martha", "Fernando"]
table4 = ["Grandma", "Dan", "Ruben", "Josie", "Lexi"]
table5 = ["Naca", "Tony", "Michael", "Angelo", "Gio"]

banquet = [table1, table2, table3, table4, table5]

print(random.choice(banquet))

# This scenario is a banquet with 5 separate tables, 5 separate lists
# and will randomly select the person that will pay out of the entire banquet

print(random.choice(banquet))

# print(len(banquet))

# print(banquet[4][1])

# print(banquet[0])
# print(banquet[1])
