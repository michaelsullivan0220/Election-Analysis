# The print() Function
# We have used the Python print() function to print the following:
# A string, or a sentence displayed between quotes. For example: print("Hello World") and 
# print("Arapahoe and Denver are not in the list of counties.").
# A string with integer values converted to a string using concatenation with the "+" sign. 
# For example: print("Your interest for the year is $" + str(interest)) .
# Both of these are sufficient when printing simple statements, but using concatenation can become 
# cumbersome when we need to print items from a list of values from a dictionary. This is where f-strings come in.


# F-strings: Formatted String Literals
# With Python 3.7, printing has become much easier with the use of f-string literals, which can be used in place
#  of concatenation. The general format for f-strings is as follows:
# The f-string begins with an f followed by a string contained within quotes. (The term f-string comes from the 
# leading "f" character preceding the string literal.)
# In the f-string, curly braces are used to add variables or expressions to the f-string.
# To see an example, let's edit the code we wrote to calculate the percentage of votes using f-string literals.
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes) + "% of the total votes.")
# And here's how you would edit the code to use f-strings.
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


# Using F-Strings with Dictionaries
# F-strings can be used to print out the keys or values of a dictionary. This will make our code 
# easier to write and read.
counties2_dict = {"Hartford": 369237, "Essex":413229, "Windham": 390222}
for county, voters in counties2_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# The output should when this code is executed should look like this:
# If we use f-stings, we can rewrite the print statement to be more intuitive and clear.
for county, voters in counties2_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
# Another use for f-strings is to print multiple strings or lines to the screen. Let's say you need 
# to tell a candidate how many votes they won, the total number of votes, and the percentage of votes 
# they received. You can use the code you wrote to calculate the percentage of votes and create a 
# message to be printed to a screen, like this:
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

# Format Floating-Point Decimals
# Notice that in the output from the algorithm above, the percentage of votes is, 14.466115988409808! 
# In Python, we can format numbers with a thousands separator and specify a decimal precision.
# The general format for a number to format it in an f-string is as follows:
# f'{value:{width}.{precision}}'
# In the format, the width specifies the number of characters used to display the value. However, if a 
# value needs more space than the width specifies, the additional space is used.
# The precision indicates the number of decimal places to format the value. For example, to format the 
# interest to two decimal places, we would use .2f, where f means "floating-point decimal format".
# When formatting a number, we can also add a thousands separator with a comma, using the following format. 
# The comma is placed after the {width}.
# f'{value:{width},.{precision}}'
# Let's add a thousands separator to the output for the candidate votes and total votes and then format 
# the percentage of votes to two decimal places. The code should look like this:
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
