############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]

# Insert for loop here
for item in myList:
    if item > 100:
        print item

# This should print [102,101,103,105]
print myList
