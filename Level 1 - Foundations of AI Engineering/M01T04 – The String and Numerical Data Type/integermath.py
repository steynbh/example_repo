# ask the user to input 3 different integers
int1 = int(input("Please enter the first integer: "))
int2 = int(input("Please enter the second integer: "))
int3 = int(input("Please enter the third integer: "))
# print the sum of the three integers
sum_integers = int1 + int2 + int3
print(f"The sum of the integers is: {sum_integers}")
# print the first integer minus the second integer
difference = int1 - int2
print(f"The difference between the first and second integers is: {difference}")
# print the first integer multiplied by the third integer
product = int1 * int3
print(f"The product of the first and third integers is: {product}")
# print the sum of all three integers divided by the third integer
if int3 != 0:  # Avoid division by zero
    division_result = sum_integers / int3
    print(f"The sum of all three integers divided by the third integer is: {division_result}")
else:
    print("Cannot divide by zero, as the third integer is zero.")
    