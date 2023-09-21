"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

elements = ["apple","pie","orange","grape" ]
print (elements)

#I just created a basic list and put some items inside 

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
elements.append ("cherry")
print (elements)

#i added a value to the list using append 
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
elements.remove ("cherry")
print(elements)

#I used the remove value to take out cherry from my list

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
elements [2] = "tomato"
print (elements)

#a list starts from 0 so by refrencing 2 i replaced orange with tomato

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
elements.append ("dragon fruit")
elements.append ("strawberry")
print (elements)

#I just appended twice and added both of them to my elements list

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del elements [3]
print (elements)
#I used del because the question asked me to delete instead of remove and i put 3 since it asked for a number in the index 
"""
Task 7: Create a new variable equal to the first 2 items of your list
Then print out the new variable.
"""
list_items = (elements[0:2])
print (list_items)

#I made a new list then just made it look into my elements list and pull out my first 2 items 

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
toppings = ["pepperoni","pineapple","cheese"]
combination = toppings + elements
print (combination)

#I made a new list and combined it with my old list elements, i made a new variable for the combination of the 2 lists and printed that out