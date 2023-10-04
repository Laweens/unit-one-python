todos = []
#The list we will be using for the assignment 

while True: 
    print("Your current To Do is. ")
    print("")
    print(todos)
    print("")
    todosadd = input("Do you wish to add or remove something from your list? ")
    #code to ask the user a basic question, giving them the option to add or remove from the "todos" list which is currently empty
    #todos add is the first question we ask the user which gives them the option, the code then stems off into add or remove
    
    if todosadd == ("add"):
        print("")
        ADD = input ("what do you want to add ")
        print("--------------------------------------------------------")
        todos.append(ADD)
    #made a new variables, ADD. ADD is an input that asks the user what they want to add
    #it then takes whatever the user enters and adds it into the list
    


    elif todosadd == ("remove"):
        print("")
        if len(todos) == 0:
            print("ERROR")
            print("")
            continue
        REMOVE = int(input("What would you like to remove? "))
        print("--------------------------------------------------------")
        print("")
        del todos[REMOVE - 1]
    #For the remove portion of the code we have to make a new variable REMOVE, similar to what we did with ADD
    #remove is the turned into an int because a list abels the items inside by an idex number starting from 0 
    #we remove 1 from the list because the user starts at 1 while the index starts at 0 
    



