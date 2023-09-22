"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""
FloatVar = 8.8
FloatVar2 = int(9.1)
print (FloatVar)
print(FloatVar2)

# I made two different variable because i wouldn't be able to print both at once if i used one variable.
#  I used int to make the float into a integer since they're not the same data type.
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
num = int(input("Say any number you can think of"))
if num > 0 : 
    print ("Thats a positive number") 
elif  num < 0 : 
    print("Thats a negative number") 
else: 
    print("The number is zero")

#since there's 3 conditions i used if to make sure that if the number was more than 0 it would say positive
#elif for the second condition to check if the number is positive 
#else is to check the rest and make sure it doesn't fill in the other two conditions


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

deci = float(input("Type in a decimal"))
num2 = int(input("type in a number "))
print (deci * num2)

# I made a variable for the first input and converted it into a float since thats what the task asked for
# I did the same thing with the second decimal and made it a float
# then i just printed the value of the float times the integer 
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

dict = {
    'apple': 10,
    'orange': 5,
    'grape': 3
}
print(dict["orange"])

#I made a dictionary and just put in fruits with different values and at the end printed it out 

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

statement = "1,2,3,4,5,6,7"
another1 = statement.split(".")

print(statement)
print(another1)
# I made one variable as a string and another into a tuple by using .split then i printed out both