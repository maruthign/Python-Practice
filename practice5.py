'''Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.'''

t=(1,2,3,4,5)
#t[1]= 23
print(t[1:3])
t1=(6,7,8)
print((t)+(t1))

'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?'''

my_fruits={"apple","banana","mango"}
friend_fruits={"apple","orange","grapes"}
print(my_fruits|friend_fruits)
print(my_fruits&friend_fruits)
print(my_fruits-friend_fruits)
my_fruits.add("kiwi")
my_fruits.discard("grapes")
my_fruits.remove("mango")
print(my_fruits)

'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?'''

l=[1,2,3,4,5]
t=tuple(l)
s=set(l)
print(t)
print(s)
#t[1]= 23
s.add(6)
print(s)