# Define a function that takes a single argument: a. A list of integers
def largest_number(numbers):
    # Base case: if the list is empty, return None
    if not numbers:
        return None
    # Recursive case: find the maximum of the first element and the largest of the rest of the list
    else:
        max_of_rest = largest_number(numbers[1:])
        return numbers[0] if max_of_rest is None or numbers[0] > max_of_rest else max_of_rest

# Ask the user to input a list of integers
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
# Call the largest_number function and print the result
result = largest_number(numbers)
if result is not None:
    print(f"The largest number in the list is: {result}")
