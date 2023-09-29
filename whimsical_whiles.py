"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
x = 1
while x <= 10:
    print(x)
    x += 1

#I made a variable to start at 1
#Then I made it so if our number is less than or equal to 10 we continue adding

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
n = 10
while n >= 1:
    print(n)
    n -= 1

#for this we did the same thing as number 1 but in a opposite order
# we start at 10 instead of 1 and we make it greater than or equal to 1 instead of 10 
#last we subtract instead of adding 

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

product = 1
fact = int(input("Pick a integer "))

while fact > 1:
    product = fact * product 
    fact -= 1 
    print(product)

#We use two variable in this exercise, 1 for the product and 1 for the number picked
# We then make it so if the number is greater than 1 we multiply.
# if they input 0 the code doesn't work because it would just be 0 as the value
# we then do the number given -1 and repeat the code
#until we are done

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = 'Pizza'

answer = input("Can you guess my password? ")

while answer != password :
    print("sorry that's not the password")
    break
else:
    print('Good job Pizza is the password')
    
#We make a password with one given value chosen by me 
#The user then tries to attempt to guess the password with as many tries as they want
# if they guess the password the code is done 

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
num = 0
n = 1
while n > 0:
    n = int(input("Enter a number, If your enter 0 the code will stop"))
    if n > 0:
        num = num + n 
        print("The sum of the numbers is", num)
    elif n == 0 :
        print("Thank you for playing")
        break

#We make two variables one as a base and one to continuosly add onto it
#The user then inputs any number they want and it adds onto the last number
#If the user inputs 0 the code is stopped 
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

