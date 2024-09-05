# Signatures1.py
# Author: Rico Jhon Mercado
# Date: September 2024

# Function to display age based on a given number of years ago
def show_age_difference(age, years_ago):
    """
    Prints the age of a person a certain number of years ago based on their current age.
    """
    # Calculate the age years_ago years ago and print it
    print(f"My age {years_ago} years ago was {age - years_ago}.")

# Define the current age
current_age = 26

# Call the function to show age 10 years ago
show_age_difference(current_age, 10)  # Outputs: My age 10 years ago was 16

# Call the function to show age 15 years ago
show_age_difference(current_age, 15)  # Outputs: My age 15 years ago was 11
