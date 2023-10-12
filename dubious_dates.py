
import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

print(datetime.datetime.now())

#a function that shows the time 


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

x = datetime.datetime.now()

print(x.strftime("%m/%d/%Y"))

#strftime gives the date time as the month, day and year since thats what i put 
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

datestr = "10 25 2006"
datestr2 = "03 05 2010"


date1 = datetime.datetime.strptime(datestr, "%m %d %Y")
date2 = datetime.datetime.strptime(datestr2, "%m %d %Y")

difference = (date2 - date1).days

print("the difference is", difference, "days")
#2 variables  are used because we need to subtract time
#we then use strftime to find the day month and year for each 

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""



