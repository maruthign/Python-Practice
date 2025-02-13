'''Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).'''

n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
s=(n1>10 and n2>10)
print(f"{n1} and {n2} both are greater than 10" , s)
 
t=n1<5 or n2<5
print("one of the number is less than 5" , t)

u=not(n1>n2)
print(f"{n1} is not greater than {n2}" , u)

'''Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.'''

age=int(input("Enter your age : "))
if (age>=18):
    print("You are an adult")
else:
    print("You are a minor")

    '''Membership Operator Exercise: Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).'''

b=input("Enter a string : ")
print("a" in b)
print("Python" not in b)

'''Bitwise Operator Task: Given two integers, write a Python program that:

Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1).'''
a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)