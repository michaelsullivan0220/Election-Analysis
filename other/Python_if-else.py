# IF ELSE statements in Python3
# The if-else statement is used when we need an outcome for both true and false conditions. 
# The if-else statement is also referred to as a dual-alternative decision statement.
# An if-else statement will execute one block of statements, or path, if a condition is true, or another 
# block of statements if the condition is false. This can be illustrated with the following flowchart.
# The if-else statement begins with the word "if," followed by a condition.
# The condition is tested.
# If the condition is true, the block of indented statements following the if statement is executed, and the 
# program moves out of the if-else statement.
# If the condition is false, the program skips to the else statement, the block of indented statements 
# following the else statement is executed, and the program moves out of the if-else statement.
# Make sure the ifstatement and the else statement are aligned.
# Make sure the statements under the if and else statements are consistently indented.

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# Nested If-Else Statements
# Sometimes, a decision structure can be more complex than a dual-alternative decision structure. 
# For instance, it's not uncommon for decision structures to be nested inside another decision structure. 
# An example of this is writing an algorithm to determine a letter grade based on a number. 
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# These nested if-else statement is quite complex and has a special name: if-elif-else statements, or the if-elif-else statement.
# With nested if-elif-else statements, we can create a compound statement, elif, in the following manner.
# The first if statement tests the condition.
# The following else statement and the preceding if statement are compounded to make the elifstatement.
# This syntax continues until the last else statement.
# In an if-elif-elsestatement, the if, elif, and elsestatements are all aligned, and the conditionally 
# executed blocks are indented.
# Using these rules for the if-elif-else statement, let's rewrite the code and run the file in the VS Code 
# terminal to determine a letter grade.

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# Compared to the nested if-elif statement, theif-elif-else statement tends to be easier to read. This is due 
# to the fact that the if, elif, and else statements are aligned, and the block statements are usually shorter.
# The length of the decision structure determines whether you use a nested if-else statement or the if-elif-else statement. 
# If you have to scroll horizontally on your computer screen to see all the code in an if-else statement , then you 
# should use an if-elif-else statement