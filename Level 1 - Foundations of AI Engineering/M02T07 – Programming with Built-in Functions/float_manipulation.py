import statistics
# ask the user to input 10 float numbers and store these numbers in a list
print("Please enter 10 numbers:")
float_numbers = []
for i in range(10):
    number = float(input(f"Number {i + 1}: "))
    float_numbers.append(number)
# calculate the sum of these numbers and print the result
total_sum = sum(float_numbers)
print (total_sum)
# find the index of the maximum number in the list and print it
max_index = float_numbers.index(max(float_numbers))
print("Index of maximum number:", max_index)
# find the index of the minimum number in the list and print it
min_index = float_numbers.index(min(float_numbers))
print("Index of minimum number:", min_index)
# calculate the average of these numbers, round it off to two decimals and print it
average = round(statistics.mean(float_numbers), 2)
print("Average of numbers:", average)
# find the median of these numbers and print it
median = round(statistics.median(float_numbers), 2)
print("Median of numbers:", median)
