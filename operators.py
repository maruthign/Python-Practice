# Assignment Operators
x=5
x+=5   # x+=5 is x=x+5
print(x)  # Output: 10
x-=3    # x-=3 is x=x-3
print(x)  # Output: 7
x*=2    # x*=2 is x=x*2
print(x)  # Output: 14
x/=2    # x/=2 is x=x/2
print(x)  # Output: 7.0
x%=2    # x%=2 is x=x%2
print(x)  # Output: 1

# Comparision Operator

x=5
y=10
print(x==y)  # Output: False
print(x!=y)  # Output: True
print(x>y)   # Output: False
print(x<y)   # Output: True

# Logical Operator
x=True
y=False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
print(not y)    # Output: True

# MemberShip Operator
x=[1,2,3,4,5]
print(1 in x)  # Output: True
print(6 in x)  # Output: False
print(1 not in x)  # Output: False
print(6 not in x)  # Output: True
print(not(1 not in x))  # Output: True

# Bitwise Operator
x=5
y=3
print(x&y)  # Output: 1  AND bitwise
print(x|y)  # Output: 7  OR bitwise
print(x^y)  # Output: 6  XOR bitwise
print(~x)   # Output: -6  NOT bitwise
print(x<<2)  # Output: 20  Left Shift
print(x>>2)  # Output: 1   Right Shift
