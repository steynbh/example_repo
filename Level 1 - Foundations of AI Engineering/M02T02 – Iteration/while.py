# continually ask the user for a number until the number entered is -1
count = 0
number = 0
sum_number = 0
while number != -1:
    number = int(input("Please enter a number (-1 to exit): "))
    # if the number is not -1 or 0, calculate the average
    if number > 0:
        count += 1
        sum_number = number + sum_number 
        # calculate the average of the numbers entered so far
        average = sum_number / count  
            # if the user enters -1, break the loop and exit
    elif number == -1:
        break
    # print the average of the numbers entered so far
print(" the average for the numbers you entered are:", average)