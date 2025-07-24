# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error fixed - missing parentheses
print ("\n") # syntax error fixed - missing parentheses and incorrect indentation

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax error fixed - incorrect indentation and == used instead of =, run error on "24 years ol" 
age = int(age_Str) 
print("I'm " + age_Str + " years old.") # Syntax error fixed - incorrect indentation

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # Syntax error fixed - incorrect indentation and string used instead of int
total_years = age + years_from_now

print ("The total number of years: " + str(total_years)) # Syntax error fixed - incorrect indentation and wrong variable name
# Changed total_years to str(total_years) to concatenate with string
# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 # Syntax error fixed - wrong variable name
print ("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old") # Syntax error fixed - missing parentheses
# runtime error fixed - added +6 to total_months to account for the 6 months and made it a string for concatenation
#HINT, 330 months is the correct answer

