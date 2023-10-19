"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def hello(self):
        print("Hi my name is " + self.name)

laweens = Person("Laweens", 16 )
laweens.hello()



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
    def speak(self):
        print()

class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount: 
    def __init__(self, Balance, Owner):
        self.Balance = Balance 
        self.Owner = Owner 
    
    def balances(self):
        print("{self.Owner} +  currently has: " + str(self.Balance))

    def withdraw(self, take):
        self.Balance = self.Balance - take
        print("your new balance is " + str(self.Balance))

    def deposit(self, dep):
        self.Balance = self.Balance + dep 
        print("Balance currently is " + str(self.Balance))

LaweensAccount = BankAccount(50000, "Laweens")

LaweensAccount.balances()
LaweensAccount.withdraw(200)
LaweensAccount.deposit(300)