# String Concatination
f_name = "Maruthi"
l_name = "Gowda"
full_name = (f"{f_name} {l_name}")
print(full_name)

# String Repetation
name = "Maruthi "
print(name * 3)

# String Methods
str = "    Hello World!   "
print(str.upper())
print(str.lower())
print(str.title())
print(str.split("2"))
print(str.strip())  # print without space
print(str.replace("World!" , "Maruthi"))

# multi line comment
a= '''Hi I'am Maruthi
I am from Bangalore
I am a Python Developer'''
print(a)
print(len(a))  #length
name = "Maruthi"
print(name[0])  #first character
print(name[-1])  #last character
print(name[0:3])  #first 3 characters
print(name[0:5])  #first 5 characters
print(name[0:])  #first all characters
print(name[:5])  #first 5 characters
print(name[1:5])  #second to fifth character
#skip or step
print(name[::2])  #skip one character
print(name[1::2])  #skip one character
print(name[::3])  #skip two character
print(name[1:5:2])  #skip two character

# Escape Sequence
sen = "maruthi \n is a good boy"  #\n is enter
print(sen)
sen = "maruthi \t is a good boy"  #\t ia tab space
print(sen)
sen = "maruthi \\ is a good boy"  #\\ is backslash
print(sen)
sen = "maruthi \a is a good boy"  #\a is bell
print(sen)
sen = "maruthi \b is a good boy"  #\b is backspac
print(sen)
sen = "maruthi \f is a good boy"  #\f is form feed
print(sen)