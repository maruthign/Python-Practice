#input and output strings
bname=input("Boy name: ")
bage=int(input("Boy age: "))
gname=input("Girl name: ")
gage=int(input("Girl age: "))

#using abs because sometimes boys might be younger
age_diff=abs(bage-gage)
# f-string formatting
print(f"{bname} loves {gname}. There age difference is {age_diff}")
print(f"{bname} is {bage} years old")
print(f"{gname} is {gage} years old")
# string formatting
print(bname+" loves "+gname+ ", There age difference is "+str(age_diff))
print(bname+" is "+str(bage)+" years old,")
print(gname+" is "+str(gage)+" years old")
# use for single line commment
'''this is a multi line comment'''