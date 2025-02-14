# Tuples and sets
# A tuple is an ordered collection of values that cannot be changed.
# A set is an unordered collection of unique values.
# Tuples and sets are both immutable, meaning they cannot be changed after they are created.

genders=("Male","Female","Others")
print(genders) 
print(type(genders))
# Accessing tuple elements
print(genders[0])
print(len(genders))
print(genders[1:3])
# Tuple methods
print(genders.count("Male"))
print(genders.index("Others"))

# Tuple concatination

tuple1=("Male","Female")
tuple2=("Others","Transgender")
print(tuple1+tuple2)

# Tuple multiplication

a=tuple1*2

# checking membership
print("Male" in tuple1)
print("Female" in tuple1)
print("Others" in tuple1)
# Tuple methods
print(a.count("Male"))
print(a.index("Female"))

# Sets
# A set is an unordered collection of unique values.
# Sets are mutable, meaning they can be changed after they are created.
# Sets are used to store a collection of unique elements.
# Sets are often used to remove duplicates from a list.

s={1,2,3,4}
print(s)
print(type(s))

#empty set
e=set()
print(type(e))

# Set methods
s.add(5)  # add 5
s.discard(10)  # remove 10 if in set
s.remove(3)  # remove 3
s.pop()  # remove random element
print(s)


#sets operation

s1={1,2,3}
s2={3,4,5}
print(s1|s2)  #union
print(s1&s2)  #intersection
print(s1-s2)  #difference
print(s1^s2)  #symmetric difference
