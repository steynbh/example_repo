# create the following list: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
numbers_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# create a linear search Implement this search algorithm to search for the number 9. Add a comment to explain why you think this algorithm was a good choice
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
# Linear search is a good choice here because the list is relatively small, and it allows us to find the target number without needing to sort the list first.
index = linear_search(numbers_list, 9)
if index != -1:
    print(f"The number 9 is found at index: {index}")

# use the the Insertion sort on this list
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
sorted_numbers = insertion_sort(numbers_list.copy())
print("Sorted list using Insertion Sort:", sorted_numbers)

# Implement a searching algorithm you haven’t tried yet in this task on the sorted list to find the number 9. Add a comment to explain where you would use this algorithm in the real world
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Binary search is efficient for large datasets where the list is sorted, as it reduces the search space by half with each iteration.
index = binary_search(sorted_numbers, 9)
if index != -1:
    print(f"The number 9 is found at index: {index}")
    