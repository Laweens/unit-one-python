# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".


def greet(name):
    print("Hello", name)

greet("THE BIG DROPPP")

#we made a function greet and gave it name as a perimeter. 
#we then simply make it print hello and whatever we make our parimeter equal to.

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

def sum(a,b):
    print( a+b)
sum(2,3)  

#made a function that takes a and b as the perimeter and adds them.
#we make our perimeter sum equal to 2 and 3 
#then a and b is added and printed 

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(num):
    n = 1
    for i in range (1,num + 1):
        n = n *1
        print("the factorial of", num, "is", n)


# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num):
    if num%2 == 0:
        print(True)
    else:
        print(False)
    
is_even(22)



# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

def calculate_area(length, width):
   print(length * width)

calculate_area( 20, 23)