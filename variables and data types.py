"""Variables"""
# variables as assigned different methods
a=10
b=20
print(a)
print(b)


a,b,c=40,30,20
print(a)
print(b)

'''variable naming rules'''
# variable names contain letters(a-z,A-Z),numbers(0-9) and underscore(_)
# variable names cannot start with a number
# variable names are case sensitive (name , Name are different)
# variable names cannot contain special characters
''' 1name=maruthi 
cannot a variable define 1name should be two words'''
_name="nirnay"
name = "maruthi"
Name = "darshan"
print(_name)
print(name)
print(Name)

'''DataTypes in python'''
#1.string
#2.integer
#3.float
#4.boolean
#5.list
#6.tuple
#7.set
#8.dictionary
#9.complex
#10.bytes
#11.bytearray
#12.memoryview
#13.range

name="maruthi"   #string
age=20           #integer
height=5.5      #float
is_adult=True   #boolean
"""Type Check"""
print(type(name))
print(type(age))
print(type(height))
print(type(is_adult))

"""Data Type Conversion"""
age1=float(age)
print(age1)
s="100"
print(int(s)+10)
print(name.upper())

'''arithmetic operations'''
# a+b  a&b are operands, + are operator
a=7
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)