"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def argue(a): #makes the function
    return a**2 #multiplies the value to the 2nd power

print (argue(2)) #calls the function
assert argue(2) == 4 #this assertion just checks to make sure 2**2 is 4 
assert argue(3) == 9 #if we were to change 2 to 3 it checks to see 3**2 is 9 


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def area(a,b): #defines the function
    return a*b #multiplies A and B by each other 
print(area(2,30)) #calls the function 
assert area(2,30) == 60 #since 2 * 30 is 60 the code continues like normal
assert area(5,10) == 50 #5*10 is 50 so if the area was equal to that the code would be true 

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def tem(c): # defines the function
    return (c * (10/2)) + 30 # retrieves the value of the function and multiplies it by 10/2 then adds 30
print(tem(1),"C") #prints the value times 1 and adds C at the end, also calls the function

assert tem(1) == 35.0 #this just checks to see if the code above gives us 35 
assert tem(2) == 40.0 #if we did 20/2 it would be 10 and 10 + 30 is 40 so its true 
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def avgN(EZ): #makes variable 
    total = sum(EZ) #calculates and retrieves the total
    avg = total / len(EZ) # finds the median of the list by taking the total and dividing it by length
    return avg #retrieves the avg 

print(avgN([10,9,8,7,6,5,4,3,2,1])) #calls function

assert avgN([1,2,3]) == 2 # I had to put a list inside the arguement to calculate the median and make sure the assertion is correct 
assert avgN([2,3,4]) == 3 # 4+3+2 is 9 and 9/3 is 3 so the median is 3 