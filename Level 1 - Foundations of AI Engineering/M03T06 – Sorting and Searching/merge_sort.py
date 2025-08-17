# design a merge sort algorithm that sorts a list of strings by string length from longest to shortest.
def merge_sort_strings_by_length(strings):
    # Get the length of the input list
    strings_length = len(strings)
    # Create temporary storage for merging
    temporary_storage = [None] * strings_length
    # Initialise the size of subsections to 1
    size_of_subsections = 1
    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < strings_length:
        for i in range(0, strings_length, size_of_subsections * 2):
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, strings_length
            )
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, strings_length
            )
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )
            merge_strings_by_length(strings, sections, temporary_storage)
        size_of_subsections *= 2
    return strings
def merge_strings_by_length(strings, sections, temporary_storage):
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0
    while left_index < first_section_end or right_index < second_section_end:
        if left_index < first_section_end and right_index < second_section_end:
            if len(strings[left_index]) > len(strings[right_index]):
                temporary_storage[temp_index] = strings[left_index]
                left_index += 1
            else:  # len(strings[right_index]) >= len(strings[left_index])
                temporary_storage[temp_index] = strings[right_index]
                right_index += 1
            temp_index += 1
        elif left_index < first_section_end:
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = strings[left_index]
                left_index += 1
                temp_index += 1
        else:  # right_index < second_section_end
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = strings[right_index]
                right_index += 1
                temp_index += 1
    for i in range(temp_index):
        strings[first_section_start + i] = temporary_storage[i]
#Run the modified Merge sort algorithm against 3 string lists of your choice. Please ensure that each of your chosen lists is not sorted and has a length of at least 10 string elements.
if __name__ == "__main__":
    strings_list1 = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon"
    ]
    strings_list2 = [
        "strawberry",
        "blueberry",
        "raspberry",
        "blackberry",
        "cantaloupe",
        "watermelon",
        "pineapple",
        "papaya",
        "mango",
        "peach"
    ]
    strings_list3 = [
        "avocado",
        "pomegranate",
        "coconut",
        "dragonfruit",
        "lychee",
        "tangerine",
        "nectarine",
        "plum",
        "quince",
        "fig"
    ]

    print("Original List 1:", strings_list1)
    sorted_list1 = merge_sort_strings_by_length(strings_list1)
    print("Sorted List 1:", sorted_list1)

    print("\nOriginal List 2:", strings_list2)
    sorted_list2 = merge_sort_strings_by_length(strings_list2)
    print("Sorted List 2:", sorted_list2)

    print("\nOriginal List 3:", strings_list3)
    sorted_list3 = merge_sort_strings_by_length(strings_list3)
    print("Sorted List 3:", sorted_list3)
