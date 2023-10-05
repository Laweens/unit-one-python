"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

inp= input('Give me a word ')

for character in inp:
    print(character)
print("")
print("-------------------------")

#we make a input that takes in any words the user gives us.
#we then use a for loop to print out each character seperately on a different line by refering to character and not inp
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

add = [1,2,3,4,8,19,122,587]
sum = 0

for num in add:
    sum += num
print("the sum of the list is", sum)

#I made two variable 1 for the sum and one for the list with random numbers in it. 
# I then use a for loop to identify each number in the list and add it to the sum of 0
#we then print the sum of 0 plus each number in the list

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

string = 'how are you? '

my_list = string.split(" ")
print(my_list)

for x in my_list:
    print(len(x))
    print("")

#we make a variable to contain the sentence that we then turn into a list using my_list.
#after we turn string into a variable we split the words in the string with .split.
#we then go back and refer to the list and print out the length of each word using len

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
cars = {
    'audi': 1,
    'bentley': 2,
    'BMW': 3,
    'Lexus': 4}

for engine in cars:
    print(engine)

#i notice that it prints all the car names that are in the dictionary
#It is what i expected because they just print in order
"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
