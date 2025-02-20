# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if both numbers are greater than 10
both_greater_than_10 = (num1 > 10 and num2 > 10)
print("Both numbers are greater than 10:", both_greater_than_10)

# Check if at least one of the numbers is less than 5
at_least_one_less_than_5 = (num1 < 5 or num2 < 5)
print("At least one number is less than 5:", at_least_one_less_than_5)

# Check if the first number is not greater than the second
first_not_greater = not (num1 > num2)
print("The first number is not greater than the second:", first_not_greater)

