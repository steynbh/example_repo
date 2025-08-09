# ask for user inputs on name, age, hair colour and eye colour of a person
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")
# create a class called Adult with the attributes name, age, hair_colour and eye_colour
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
    # create a method called can_drive which prints the name of the person and that they are old enough to drive
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

# create a subclass of Adult named Child that have the same attributes as Adult but overrides the can_drive method to print the persons name and that they are not old enough to drive
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is not old enough to drive.")

# create the logic to check if the person is 18 years or older and create an instance of the Adult class if its true, otherwise create an instance of the Child class
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)
# call the can_drive method on the person object
person.can_drive()