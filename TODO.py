todos = []

while True: 
    print("your current list of todos are ")
    print(todos)
    input("would you like to add or remove from your list?")
    if input == 'add':
        todos.append(input("What would you like to add to the To Do list "))
        continue
    else:
        int(input("which item number would you like to remove from the list"))
        todos.remove(input -1)


