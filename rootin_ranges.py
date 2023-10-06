"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

for p in range(1,11):
    print(p)
    print("---------------------------------")
    print("")

#I made a for loop and put 1-11 in the range to print 1-10
# i picked 11 instead of 10 because the index starts at 0 so it's one less 

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for y in range(900,1010,10):
    print(y)
    print("---------------------------------")
    print("")

#it's similar to number 1 but now we add increments by adding a 3rd value which is what the code increments by
#now the code goes from 900 to 1000 by increments of 10 the 3rd value in the range

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for z in range(1,109,9):
    print(z)
    print("---------------------------------")
    print("")

#like number 2 we make a for loop and give it a range from 1-109 and increments by 9
# i put 109 so the code doesn't stop counting at 91 

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
sum = 0

for num in range(1,10):
    sum += num
print("the sum of the list is", sum)
print("---------------------------------")
print("")      

#I made a variable for the sum then made a for loop that has a range from 1-10
# for every number in the range it adds to the sum which is 0
#the code adds 1 to 0 then 2 to 1 since the sum is 1 and it continues like that until 10 




"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
    print()

#The output of the following code is Astericks being printed in multiple rows and adding 1 each time 
#the code refers back to the variable rows as it's range and loops 5 times, 
# then each time refers to the row the code add's 1 to the amount of astericks and end's with a spance then starting on a new line
