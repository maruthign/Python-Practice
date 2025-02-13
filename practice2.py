'''Simple Greeting Program: 
Write a Python program that asks the user for their name and age,
 then prints a personalized greeting message.
 Use both the + operator and f-strings for output.'''

name=input("Enter your name : ")
age=int(input("Enter your age : "))
print(f"Hello, my name is {name}. Iam {age} years old")
print("Hello, my name is " + name + ". Iam "+ str(age) +" years old")

'''String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.'''

sen=input("enter a sentence : ")
print(sen.upper())
print(sen.lower())
print(sen.replace(" ","_"))
print(sen.strip())
print(sen.title())

'''Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces'''

s=input("enter a string : ")
print(len(s.replace(" ","")))


'''Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
Example:

Hello
    World
This is a backslash: '''
print("Hello\n \tWorld \nThis is a backslash: \\")
