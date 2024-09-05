# Signatures1.py
# Author: A. N. Other
# Date: September 2024

# Function to display age based on a given number of years ago
def show_age_difference(age, years_ago):
    """Prints the age a certain number of years ago."""
    print(f"My age {years_ago} years ago was {age - years_ago}.")

# Call the function for current age and age 15 years ago
current_age = 26
show_age_difference(current_age, 10)  # My age 10 years ago
show_age_difference(current_age, 15)  # My age 15 years ago
