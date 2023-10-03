todos = []

option = input("would you like to add or remove from your list? ")

while True: 
    print("your current list of todos are ")
    print("")
    print(todos)
    print("")
    print("")
    if option == 'add':
        todos.append(input("What would you like to add to the To Do list "))
    elif option == 'remove':
        print("What would you like to remove from the list")
        
        
        


