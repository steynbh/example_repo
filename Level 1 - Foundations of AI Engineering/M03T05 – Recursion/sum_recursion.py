# Define a function which takes two arguments: a. A list of integers. b. A single integer that represents an index point.
def sum_recursion(numbers, index):
    # Base case: if the index is less than 0, return 0
    if index < 0:
        return 0
    # Recursive case: add the current number to the sum of the previous numbers
    else:
        return numbers[index] + sum_recursion(numbers, index - 1)

# ask user to input a list of integers and a single integer that represents the last index of the list
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
last_index = int(input("Enter the last index of the list (0-based): "))
# Check if the last index is valid and if not valid loop to ask for a valid index
while last_index < 0 or last_index >= len(numbers):
    print("Invalid index. Please enter a valid index.")
    last_index = int(input("Enter the last index of the list (0-based): "))
# If the last index is valid, call the sum_recursion function and print the result
result = sum_recursion(numbers, last_index)
print(f"The sum of the numbers from index 0 to {last_index} is: {result}")
