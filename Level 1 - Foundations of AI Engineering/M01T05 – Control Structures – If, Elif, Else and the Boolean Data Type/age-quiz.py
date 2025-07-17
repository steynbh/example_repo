# ask the user to input their age
age = int(input("Please enter your age: "))
# if the user is over 100 print sorry you're dead
if age > 100:
    print("Sorry, you're dead.")
# else if the user is over 40 print you are over the hill
elif age >= 40 and age < 65:
    print("You are over the hill.")
# else if the user is equal to or over 65 print enjoy your retirement
elif age >= 65:
    print("Enjoy your retirement.")
# else if the user is under 13 print you qualify for kiddies discount!
elif age < 13:
    print("You qualify for kiddies discount!")
# else if the user is equal to 21 print congrats on your 21st
elif age == 21:
    print("Congrats on your 21st!")
# else print age is but a number
else:
    print("Age is but a number.")