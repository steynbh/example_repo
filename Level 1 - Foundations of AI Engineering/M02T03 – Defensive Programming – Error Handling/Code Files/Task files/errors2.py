# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # add parentheses to string variable
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 
# logial error:change the variable names around to ensure the right output
# run time error - add f-string formatting

print(full_spec) # Syntax error fixed - missing parentheses

