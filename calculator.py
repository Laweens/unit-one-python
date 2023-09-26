uno = float(input("Put in your first number"))
dos= float(input("Enter your second number"))
# two variables so the user can do whatever operation they want to do between them 
print("select operation:")
print("1. Addition")
print("2. subtraction")
print("3. multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
#Gives the user a list of the options they have available
op = input ("Pick an operation ")

if op == '1' :
    print(uno + dos)
elif op == '2' :
    print(uno - dos)
elif op == '3' :
    print(uno * dos)
elif op == '4' :
    if dos == 0 : 
        print ("I cannot calculate that number")
    else:
        print(uno / dos)
elif op == '5' :
    print(uno // dos)
elif op == '6' :
    print(uno ** dos)
elif op == '7' :
    print(uno % dos)
# I put 7 conditions because there's 7 different operations they can do 
#Each condition is almost exactly the same except the operation is changed
#For the divison operation I made it so the user is told they can't divide by 0 

