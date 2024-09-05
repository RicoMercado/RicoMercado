# Getting Data from Functions
# Challenge 2 (Use a function to get the sum of two numbers)
# date: November 2016
score = 0
print('\nSumming Two Numbers')
def get_sum(num1, num2):
sum = num1 + num2
return sum
num1 = int(input('\nEnter the first number: '))
num2 = int(input('\nEnter the second number: '))
print('\nThe sum of {0} and {1} is {2}'.format(num1, num2, get_sum(num1,
num2)))
