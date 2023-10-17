while True: #I use a loop to end the code after the user puts in a string instead of an int 
    try: #we put the try before the problem code
        age = int(input('Enter your age: ')) #input to ask for code 
    except: #we put the except after the problem code 
        print("That is a string, please try again and input a integer") #code that's printed after a string is input 
        break #we use a break so the code doesn't continue if they put a string 
    faveNum = int(input('What is your favorite number: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
    try:
        print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
    except: print("we cannot divide your favorite number by 0")
    #we put a try and except around the division because dividing by 0 is a error we want to e=avoid 