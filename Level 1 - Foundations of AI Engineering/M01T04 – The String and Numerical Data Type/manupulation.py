# ask the user to input a sentence
str_manip = input("Please enter a sentence: ")
# calculate the display length of the string
display_length = len(str_manip)
# find the last letter in the string and replace every occurrence of it with a "@""
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, "@")
# print the last three caracters of the string backwards
last_three = str_manip[-3:][::-1]
# create a 5 letter word that is made up of the first 3 caracters and the last two characters of the string
first_three = str_manip[:3]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two
# print the word made up of the first three and last two characters
print(f"Five letter word: {five_letter_word}")