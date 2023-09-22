'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''

num = int (input("Enter any number"))
if num % 2 == 0: 
    print("That is an even number")
else: print("that is an odd number")


#I used the % because it returns the remainder of the dividend so it there's no remainder it must be a even number

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
try:
 num = int(input("Say any number you can think of"))
except ValueError:
 print("Invalid Input")
if num > 0 : 
    print ("Thats a positive number") 
elif  num < 0 : 
    print("Thats a negative number")  
else: 
    print("The number is zero")

#since there's 3 conditions i used if to make sure that if the number was more than 0 it would say positive
#elif for the second condition to check if the number is positive 
#else is to check the rest and make sure it doesn't fill in the other two conditions


'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
list = max(1,2,3,50)
print(list)
# I made a list and just made it retrieve the highest value by putting max next to it
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
year = int(input("what year is it?"))
if year % 4 == 0 : 
    print("It is a leap year")
else:
    print("it is not a leap year")

 #since a leap year is 4 year's i decided to divide the year by 4 and if there's no dividend it has to be a leap year 

'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''
vowel = input("Pick a letter in the alphabet")
if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" :
    print("That is a vowel") 
else: print("that is a consonant ")

#there's 26 letters in the alphabet, 5 of them are vowels, the other 21 are consonants
# I just seperated the vowels into a list and coded it so if they entered something in the list it's deemed a vowel