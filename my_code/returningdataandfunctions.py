# ReturningDataandFunctions.py
# Author: Rico Jhon Mercado
# Date: September 2024

# Define a function to calculate the sum of two numbers
def get_sum(num1, num2):
    # Return the result of adding num1 and num2
    return num1 + num2

# Print a message to indicate the start of the program
print('\nSumming Two Numbers')

# Prompt the user to enter the first number and convert it to an integer
num1 = int(input('\nEnter the first number: '))

# Prompt the user to enter the second number and convert it to an integer
num2 = int(input('\nEnter the second number: '))

# Print the result of the sum, formatted to show the user the numbers and their sum
print(f'\nThe sum of {num1} and {num2} is {get_sum(num1, num2)}')
