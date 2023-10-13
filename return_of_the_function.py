"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def argue(a): #makes the function
    return a**2 #multiplies the value to the 2nd [ower]

print(argue(25)) #calls the function



"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def area(a,b): #defines the function
    return a*b #multiplies A and B by each other 
print(area(2,30)) #calls the function 


"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def tem(c): # defines the function
    return (c * (10/2)) + 30 # retrieves the value of the function and multiplies it by 10/2 then adds 30
print(tem(1),"C") #prints the value times 1 and adds C at the end, also calls the function


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
