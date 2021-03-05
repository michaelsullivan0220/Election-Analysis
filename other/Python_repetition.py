# When writing an algorithm that performs the same task over and over, it's a lot 
# easier to write the code for the algorithm once, and then place that algorithm 
# in a repetition structure that can be repeated as many times as necessary. 
# This type of repetition structure is called a loop.
# There are two categories of repetition structures: condition-controlled loops 
# and count-controlled loops.
# A condition-controlled loop uses a true or false condition to control the number of 
# times that it repeats, like asking a user if they want to continue with their online 
# shopping after they add something to their "basket." This type of loop is also called 
# a while loop.
# A count-controlled loop repeats a specific number of times depending on the conditions, 
# such as getting all the items in a list. This type of loop is also called a for loop.


# While loops test if a condition is true. If the condition is true, then the code will 
# perform a task. This type of loop has two parts:
# A condition that is tested for a true or false value.
# A statement or statements that are repeated as long as the condition is true.
x = 0
while x <= 5:
    print(x)
    x = x + 1
# We set the variable x = 0 before we enter the loop.
# We test if x is less than or equal to 5.
# If this condition is true, then we print the value of x.
# With x = x + 1, we increment x by 1.
# The condition is tested again
# We repeat this process until the condition is false. When x is greater than 5, the loop stops.


# For Loops
# For loops iterate, or run through, a program a specific number of times before it stops. 
# A for loop can be written like if and if-else statements. Here's the general format:
#  for item in [items]:
#    statement 1
#    statement 2
# There is a for statement, followed by an item or variable that is found in a list of items of an 
# unknown number. The items can be a list, as in the previous code block example, or a tuple or dictionary.
# Upon the first iteration, the item will be the first item in a list. The second iteration will be the 
# second item in the list, and so on. The statements that follow will be executed as long as the number of 
# items has not been exhausted. When there are no more items in the list, the for loop stops.


# Iterate Through Lists and Tuples
counties = ["Hartford", "Essex", "Windham"]
for county in counties:
    print(county)
# When we execute this code, the county variable is declared and set equal to the first item in the list of 
# counties, "Arapahoe." Then we print the first item, "Hartford," to the screen. For the second iteration,
# the county variable is set equal to "Essex," and then "Windham" is printed. This process continues for the 
# number of items in the list of counties.
# Python has a built-in function, range(), that simplifies the process of writing a for loop. 
# The range() function creates an iterable object or a list. For example, if we had a list of numbers, 
# we could print each number using a for loop like this:
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
# When this code is executed, all the numbers in the list would be printed to the screen.
# We will get the same output if we simplify the code by modifying the for loop, using the range() function:
for num in range(5):
    print(num)
# Indexing can also be used to iterate through a list. If the list contains strings, we'll need to get the 
# length of the list as an integer for the range() function. For example, to iterate through the counties 
# list using the range() function, the code should be rewritten as follows:
for i in range(len(counties)):
    print(counties[i])
# The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. 
# The letter i is often used for simplicity, but any variable can be used.
# Inside the range() function, we get the length of the list of counties, which is the integer 3.
# Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed 
# into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
# This process is continued until all three items, or counties, in the list are printed to the screen.


# Iterate Through a Dictionary
# We can use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys 
# and values. To practice getting the keys and values from a dictionary, we will use the counties dictionary 
# that was created earlier:
counties2_dict = {"Hartford": 422829, "Essex": 463353, "Windham": 432438}

# 1) Get the Keys of a Dictionary
# To get only the keys from a dictionary using a for loop, the loop can be written like we are iterating 
# over a list or tuple.
for county in counties2_dict:
    print(county)
# When we execute this code, we get the counties printed to the screen.
# We can also use the keys() method to iterate over a dictionary to get the keys. To the previous code, 
# add the keys() method to the end of the counties_dict, like this:
for county in counties2_dict.keys():
    print(county)
# When using the keys() method, it doesn't matter what variable name we use in the for loop. 
# The keys() method will print each key in order.

# 2) Get the Values of a Dictionary
# To get the values of a dictionary, we iterate over the dictionary using the values() method, just like we 
# used the keys() method.
for voters in counties2_dict.values():
    print(voters)
# Also, when using the values() method, it doesn't matter what variable name we use in the for loop. 
# The values() method will print each value in order.
# When using the format dictionary_name[key], include the key county in the for loop in the print statement. 
# This will return the value of the key in the output.
# For the counties list, modify the for loop and use the key, county to reference the value.
for county in counties2_dict:
    print(counties2_dict[county])
# Another method we can use to get the values of a key is to use the get() method on the dictionary in the for loop.
for county in counties2_dict:
    print(counties2_dict.get(county))

# 3) Get the Key-Value Pairs of a Dictionary
# Finally, if we want to print the key-value pair of the dictionary, we use the items() method in the for loop, which 
# follows this general format:
for key, value in counties2_dict.items():
    print(key, value)
# When we use the items() method, we get the key and the value for each dictionary by referencing them as "key" and
# "value" as in the code above, or we can reference them by name, like "county" and "voters", as in the code below.
for county, voters in counties2_dict.items():
    print(county, voters)
# When we execute this code in the VS Code terminal, the output will be each key and value in order.
# When iterating over a dictionary:
# The first variable declared in the for loop is assigned to the keys.
# The second variable is assigned to the values.

# 4) Iterate Through a List of Dictionaries
# A for loop can be used to iterate through a list of dictionaries like our voting_data list of dictionaries we 
# created earlier. With a for loop we can:
# Retrieve each dictionary in the list
# Retrieve only the values of each dictionary
# Retrieve the key-value pairs of each dictionary
# Get Each Dictionary in a List of Dictionaries
# To print each dictionary in voting_data, use the standard format for iterating over the list of dictionaries with a for loop:
voting_data = [{"county":"Hartford", "registered_voters": 422829},
                {"county":"Essex", "registered_voters": 463353},
                {"county":"Windham", "registered_voters": 432438}]
for counties2_dict in voting_data:
    print(counties2_dict)
# or 
for i in range(len(voting_data)):
    print(voting_data[i])

# 5) Get the Values from a List of Dictionaries
# To retrieve only the values from each dictionary in the list of dictionaries, we need to use a nested for loop. 
# Let's see how this can be done with our voting_data.
# First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. Then, in the second 
# for loop, use the values() method on the variable county_dict to reference the data in the second for 
# loop in order to get each value.
for counties2_dict in voting_data:
    for value in counties2_dict.values():
        print(value)

# Just get voter data
for counties2_dict in voting_data:
    print(counties2_dict['registered_voters'])

# If we only want to print the county name from each dictionary, we can use county_dict['county'] 
# in the print statement for the for loop.
for counties2_dict in voting_data:
    print(counties2_dict['county'])