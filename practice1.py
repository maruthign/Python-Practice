a=19
b=20
print (a//b)
a,b=b,a
print(b)
print(type(a))
c=str(a)
print(type(c))
print(c+str(b))
name="MARUTHI"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.swapcase())
print(name.casefold())
print(name.center(15,"1"))
print(name.ljust(10,"*"))
print(name.rjust(10,"*"))
print(name.zfill(10))

bn=input("Enter boy name: ")
ba=int(input("boy age: "))
gn=input("Enter girl name: ")
ga=int(input("girl age: "))
print(f"{bn} loves {gn}")
ad=abs(ba-ga)
if ba==ga:
    print(f"{bn} and {gn} both are same age")
elif ba>ga:
    print(f"{bn} is {ad} years older than {gn}")
else:
    print(f"{bn} is {ad} years younger than {gn}")
a="3"
print(a*3)