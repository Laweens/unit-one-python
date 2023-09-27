'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

num = int(input("Pick a random whole number"))

if num >= 10 and num % 2 == 0 : 
    print("True")
else:
    print("False")

#Were checking if the value submited is equal to or greater than 10 with the first condition 
#then we check if the value given to us is even by checking if there's a remainder left when divided by 2 
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age= int(input("What is your Age?"))
print("Answer Yes or No")
status = input("Are you currently a student ")

if age < 18 or status == "Yes" :
    print("Price is $10")
else:
    print("The price is $20")
#We have to check if they are of age then we check if they are currently a student with the condition
#Then if both conditions are true we make the price $10 otherwise its 20

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruit = ['Apple','Tomato','Pear','Dragon fruit','Orange','Peach']
picker = input("Pick a fruit ")

if picker in fruit :
    print('Yes, that fruit is in the list')
else:
    print("No, that is not a fruit in the list")

#We make a list then we ask the user to pick a fruit
#We check with the condition if the fruit the user picked is in the list and print based off the value 
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year = int(input("what year is it?"))
if year % 4 == 0 and year % 100 == 0 : 
    print("It is a leap year and a century year")
else:
    print("it is not a leap year and century year")

#we check the year first, then we divide it by 4, if it has no remainder its a leap year
#we do the same for the year but divide it by 100 to check if its a century 

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight = int(input("What is the weight of your package"))

zone = input("Are you shipping in zone A or B ? ")

if weight == 0 : 
     print ("ERROR")
elif zone == 'A':
    print(weight * 5)
else:
    print(weight * 7)

#first we see if the weight of the package is 0 and give them an error
# if the value isn't zero we multiple the weight by whatever zone they said they are in, either 5 or 7 times the weight


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

side1 = int(input("What is the length of side 1? "))
side2 = int(input("What is the length of side 2? "))
side3 = int(input("What is the length of side 3? "))

if side1 == side2 and side2 == side3 and side1 == side3:
    print('Thats an Equilateral')
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("Thats a scalene triangle")
elif side1 == side2 and side2 == side3 and side1 != side3:
    print("Thats an Isoceles triangle")
else: 
    print("thats not a triangle")

#i had to find how long each side of the triangle is and give it equal or unequal values depending on it.