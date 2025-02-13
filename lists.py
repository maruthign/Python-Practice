# list
'''A list is a collection of items that are ordered,
mutable (changeable), and allow duplicate elements.
Lists can hold items of different data types,
such as integers, strings, or even other lists.'''

items=["apple",[1,2,3],1,True,"banana", "orange","banana"]
print(items)
print(items[0]) # prints: apple
print(items[-1]) # prints: banana
items.pop()  # last element as removed
print(items)
items.pop(0) # first element as removed
print(items)
items.append("grape") # adds "grape" at the end
print(items)
items.insert(0,"banana") # adds "pear" at the beginning
print(items)
items.remove("banana") # removes the first occurrence of "banana"   
print(items)
items [1] = 2
print(items)
items.clear()
print(items)

# list slicing
numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers)
print(numbers[0:3]) # prints: [0, 1, 2]
print(numbers[0:3:2]) # prints: [0, 2]
print(numbers[0:]) # prints: [0, 1, 2, 3,
print(numbers[:]) # prints: [0, 1, 2, 3,
print(numbers[0:10:2]) # prints: [0, 2, 4
print(numbers[::2]) # prints: [0, 2, 4, 6
print(numbers[1::2]) # prints: [1, 3, 5,

# length of lists
items=[1,35,65,76,45,34,76,True,]
print(len(items)) # prints: 7
# sorted
print(sorted(items))
#sum
print(sum(items))

# Common Metods
a=[1,2,1,3,2,3,2,3,6,8,5,2,6]
print(a.count(2)) # prints: 4
print(a.index(2)) # prints: 1
print(a.index(2,3)) # prints: 4
print(a.index(2,3,5)) # prints: 4
b=[1,3,2,3,5,35,343,23]
print(sorted(b))
print(sorted(b,reverse=True))
print(b.sort())

#nested lists
c=[[1,2,3],[4,5,6],[7,8,9]]
print(c[0][1]) # prints: 2
print(c[1][2]) # prints: 6
print(c[2][0]) # prints: 7
print(c[0][0:2]) # prints: [1, 2]
print(c[1][1:3]) # prints: [5, 6]
print(c[2][1:3]) # prints: [8, 9]
print(c[0][0:2]+c[1][1:3]) # prints:[1,2,5,6]