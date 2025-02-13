'''List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.'''
# Create a list of 5 items
list = [1, 2, 3, 4, 5]
print(list.append(6))
print(list.insert(1, 7))
print(list.pop(2))
print(list)  # Output: [1, 7, 4, 5,

'''Reverse and Sort a List: Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it.'''
# Create a list of numbers
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)